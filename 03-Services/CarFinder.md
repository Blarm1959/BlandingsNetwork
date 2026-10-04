# CarFinder LXC recovery leads

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### Additional LXC: CarFinder (S25/S26)

**HISTORICAL USER EVIDENCE, 3 October 2026:** shell prompts show `root@carfinder:/opt/carfinder` and `.venv` use. User test output records successful external Ford API responses. This is evidence of an application host/path and outbound access at that time, not proof of its current network address or container ID.

The user explicitly identifies the CarFinder LXC update command as `cd /opt/carfinder && bash admin/update_lxc.sh` (S26). It is preserved as the named project workflow, not executed by this audit.

Assistant summaries name `carfinder-streamlit.service`, app endpoint `http://10.83.59.181:8501`, and Laptop 1 `INV-LAP-01` with repository folder `D:\Git\Repos\Blarm1959`. These are specific recovery candidates, not freshly verified values. The endpoint is outside the confirmed main LAN `10.59.0.0/16`; its date does not justify replacing the current baseline or assuming another active subnet. Verify where this LXC runs, its actual address/CTID, service/listener, routes and current version. Do not convert the endpoint into a new address-group recommendation.
## Address-generation context from HomeNetwork (S27)

Copied common_vars and a backup folder document a historical 10.83 generation. This gives context for the assistant endpoint 10.83.59.181, but does not prove the CarFinder host used that generation, resolve its present address or supersede the user's confirmed10.59 baseline. Keep V17 open.
