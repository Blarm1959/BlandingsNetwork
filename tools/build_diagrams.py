"""Rebuild repository diagrams and marked Markdown blocks from JSON source."""
import argparse
from io import BytesIO
import json
import math
from pathlib import Path
import re
import sys

try:
    from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon
    from reportlab.graphics import renderSVG, renderPDF
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4, landscape
except ImportError:
    raise SystemExit('ReportLab is required. Install tools/diagram-requirements.txt with your Python interpreter; see diagrams/README.md.')

NAVY = HexColor('#13263B')
MUTED = HexColor('#586A7D')

def text(d, x, y, s, size=12, color=NAVY, font='Helvetica', anchor='start'):
    d.add(String(x,y,s,fontName=font,fontSize=size,fillColor=color,textAnchor=anchor))

def safe_path(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f'Path outside repository: {relative}')
    return path

def validate(data):
    if data.get('schema_version') != 1:
        raise ValueError('Unsupported diagram schema_version')
    for key in ('id','title','source','status','notes','record_path','output_basename'):
        if key not in data: raise ValueError(f'Missing {key}')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', data['output_basename']):
        raise ValueError('Unsafe output_basename')
    if data['kind'] == 'port-grid':
        count = data['port_count']
        numbers = [p['number'] for p in data['ports']]
        if sorted(numbers) != list(range(1,count+1)):
            raise ValueError('Each numbered port must occur exactly once')
        flat = [n for row in data['rows'] for n in row]
        if sorted(flat) != sorted(numbers): raise ValueError('Row layout must include every port exactly once')
        if len(data['rows']) != 2 or any(len(row) > 9 for row in data['rows']):
            raise ValueError('Port-grid renderer supports two rows of at most nine ports')
        for p in data['ports']:
            label = p['destination']
            if label is not None and (not isinstance(label,str) or not label.strip() or len(label)>16):
                raise ValueError('Destinations must be null or short non-empty labels')
    elif data['kind'] == 'topology':
        ids = [n['id'] for n in data['nodes']]
        if len(ids) != len(set(ids)) or not ids: raise ValueError('Unique node IDs required')
        for n in data['nodes']:
            if not re.fullmatch('[A-Za-z][A-Za-z0-9_]*',n['id']): raise ValueError('Invalid Mermaid node ID')
            if not (90<=n['x']<=752 and 125<=n['y']<=440): raise ValueError('Node position outside chart area')
            lines=n['label'].splitlines()
            if len(lines)>2 or any(len(line)>26 for line in lines): raise ValueError('Node label too long')
        for edge in data['edges']:
            if edge['from'] not in ids or edge['to'] not in ids or edge['from']==edge['to']:
                raise ValueError('Edge must refer to two known distinct nodes')
    else: raise ValueError('Supported kinds: port-grid, topology')

def base(data):
    d = Drawing(842,595)
    d.add(Rect(0,0,842,595,fillColor=HexColor('#FFFFFF'),strokeColor=None))
    text(d,34,542,data['title'].upper(),12,HexColor('#007C91'),'Helvetica-Bold')
    text(d,34,504,data['subtitle'],29,NAVY,'Helvetica-Bold')
    sub = f"{data['model']}  |  Original port-connection record" if data['kind']=='port-grid' else data['status']
    text(d,34,479,sub,12,MUTED)
    d.add(Line(34,97,808,97,strokeColor=HexColor('#D6DFE9'),strokeWidth=.8))
    text(d,34,76,'SOURCE  '+data['source'],8,MUTED)
    for index,note in enumerate(data['notes']):
        text(d,34,58-14*index,note,8,MUTED)
    return d

def port_grid(data):
    d=base(data)
    ports={p['number']:p['destination'] for p in data['ports']}
    d.add(Rect(32,154,778,298,rx=14,ry=14,fillColor=HexColor('#F3F6FA'),strokeColor=HexColor('#D6DFE9'),strokeWidth=1))
    text(d,46,431,'TOP ROW / ODD-NUMBERED PORTS',9,MUTED,'Helvetica-Bold')
    text(d,46,304,'BOTTOM ROW / EVEN-NUMBERED PORTS',9,MUTED,'Helvetica-Bold')
    for row,nums in enumerate(data['rows']):
        y=321 if row==0 else 192
        for col,number in enumerate(nums):
            x=46+col*84; label=ports[number]
            accent=HexColor('#1679A8') if label=='Loft' else HexColor('#078678') if label and label.startswith('Study') else HexColor('#B86A12') if label=='neoHub' else NAVY if label else HexColor('#9BA9B8')
            d.add(Rect(x,y,76,98,rx=7,ry=7,fillColor=HexColor('#FFFFFF'),strokeColor=HexColor('#CDD7E2'),strokeWidth=.8))
            d.add(Rect(x+8,y+90,60,3,fillColor=accent,strokeColor=None))
            text(d,x+38,y+63,str(number),25,accent,'Helvetica-Bold','middle')
            d.add(Rect(x+25,y+32,26,21,rx=2,ry=2,fillColor=HexColor('#EAF0F5'),strokeColor=HexColor('#75879A'),strokeWidth=.6))
            for pin in range(6): d.add(Line(x+29+pin*3,y+45,x+29+pin*3,y+50,strokeColor=HexColor('#75879A'),strokeWidth=.7))
            text(d,x+38,y+13,label or 'Not specified',9 if label else 8,accent if label else MUTED,'Helvetica-Bold' if label else 'Helvetica','middle')
    known=sum(label is not None for label in ports.values())
    text(d,34,118,f'{known} labelled connections',11,NAVY,'Helvetica-Bold')
    text(d,210,118,f'{len(ports)-known} ports without a destination in the original message',11,MUTED)
    return d

def topology(data):
    d=base(data)
    nodes={n['id']:n for n in data['nodes']}
    for edge in data['edges']:
        a,b=nodes[edge['from']],nodes[edge['to']]
        dx,dy=b['x']-a['x'],b['y']-a['y']
        scale=1/max(abs(dx)/83,abs(dy)/26)
        ax,ay=a['x']+dx*scale,a['y']+dy*scale
        bx,by=b['x']-dx*scale,b['y']-dy*scale
        d.add(Line(ax,ay,bx,by,strokeColor=HexColor('#7594AC'),strokeWidth=1.5,strokeDashArray=[4,3]))
        length=math.hypot(dx,dy); ux,uy=dx/length,dy/length
        d.add(Polygon([bx,by,bx-8*ux+3*uy,by-8*uy-3*ux,bx-8*ux-3*uy,by-8*uy+3*ux],fillColor=HexColor('#7594AC'),strokeColor=None))
        if edge.get('label'):
            lx,ly=(ax+bx)/2+12,(ay+by)/2+9
            d.add(Rect(lx-4,ly-3,46,15,fillColor=HexColor('#FFFFFF'),strokeColor=None))
            text(d,lx,ly,edge['label'],9,HexColor('#1679A8'),'Helvetica-Bold')
    for n in data['nodes']:
        d.add(Rect(n['x']-83,n['y']-26,166,52,rx=8,ry=8,fillColor=HexColor('#F3F6FA'),strokeColor=HexColor('#CDD7E2'),strokeWidth=.8))
        lines=n['label'].splitlines()
        for i,line in enumerate(lines): text(d,n['x'],n['y']+(6 if len(lines)==2 else -3)-i*15,line,10,NAVY,'Helvetica-Bold' if i==0 else 'Helvetica','middle')
    return d

def markdown(data):
    if data['kind']=='port-grid':
        rows=['| Numbered port | Room / destination in original message |','|---:|---|']
        for p in sorted(data['ports'],key=lambda p:p['number']):
            label=(p['destination'] or 'Not specified').replace('|','\\|')
            rows.append(f"| {p['number']} | {label} |")
        return '\n'.join(rows)
    lines=['```mermaid','flowchart TD']
    for n in data['nodes']:
        label=n['label'].replace('\n',' / ').replace('"',"'")
        lines.append(f'  {n["id"]}["{label}"]')
    for edge in data['edges']:
        connector=f' -. "{edge["label"]}" .-> ' if edge.get('label') else ' -.-> '
        lines.append('  '+edge['from']+connector+edge['to'])
    lines.append('```')
    return '\n'.join(lines)

def outputs(data):
    d=port_grid(data) if data['kind']=='port-grid' else topology(data)
    svg=renderSVG.drawToString(d)
    if isinstance(svg,str): svg=svg.encode('utf-8')
    buffer=BytesIO()
    c=canvas.Canvas(buffer,pagesize=landscape(A4),invariant=1)
    c.setTitle(data['title']);c.setAuthor('BlandingsNetwork')
    renderPDF.draw(d,c,0,0);c.showPage();c.save()
    return {'svg':svg,'pdf':buffer.getvalue()}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--diagram',default='all')
    parser.add_argument('--check',action='store_true',help='Check generated files/marked blocks without writing them')
    args=parser.parse_args(); root=args.root.resolve()
    sources=sorted((root/'diagrams/source').glob('*.json'))
    selected=[]
    for source in sources:
        data=json.loads(source.read_text(encoding='utf-8-sig'))
        if args.diagram=='all' or data['id']==args.diagram: selected.append((source,data))
    if not selected: raise ValueError(f'No diagram sources found for {args.diagram}')
    # Validate and render all selected items before any file is written.
    plans=[]
    for source,data in selected:
        validate(data)
        path=safe_path(root,data['record_path'])
        current=path.read_text(encoding='utf-8-sig')
        start=f'<!-- DIAGRAM:{data["id"]}:BEGIN -->'; end=f'<!-- DIAGRAM:{data["id"]}:END -->'
        if current.count(start)!=1 or current.count(end)!=1 or current.index(start)>=current.index(end):
            raise ValueError(f'Missing/ambiguous generation markers in {path}')
        replacement=start+'\n'+markdown(data)+'\n'+end
        revised=re.sub(re.escape(start)+r'.*?'+re.escape(end),lambda _:replacement,current,flags=re.S)
        files={safe_path(root,'diagrams/'+data['output_basename']+'.'+ext):body for ext,body in outputs(data).items()}
        if data['kind']=='topology':
            files[safe_path(root,'diagrams/'+data['output_basename']+'.mmd')]=(markdown(data).removeprefix('```mermaid\n').removesuffix('\n```')+'\n').encode('utf-8')
        plans.append((data,path,current,revised,files))
    stale=[]
    for data,path,current,revised,files in plans:
        if args.check:
            if current!=revised: stale.append(str(path.relative_to(root)))
            for output,body in files.items():
                if not output.exists() or output.read_bytes()!=body: stale.append(str(output.relative_to(root)))
        else:
            for output,body in files.items(): output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(body)
            if current!=revised: path.write_text(revised,encoding='utf-8',newline='\n')
            print(f'Built {data["id"]}: PDF, SVG, marked record'+(', Mermaid' if data['kind']=='topology' else ''))
    if stale: raise ValueError('Generated content out of date: '+', '.join(stale))
    if args.check: print(f'Checked {len(plans)} diagram sources; generated files and record blocks match.')

if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr);sys.exit(1)
