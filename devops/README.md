# True Tech Sprint: DevOps

Five Kubernetes engineering tasks, each solved and verified live on a real cluster. The sprint is judged on solving speed and correctness — solutions are reviewed by hand by MWS experts after the deadline (no automated acceptance tests), so each solution must actually work in the cluster.

## Tasks

| # | Task | What it is | Statement | Solution |
| --- | --- | --- | --- | --- |
| 1 | GitLab Runner | Deploy a GitLab Runner (k8s executor) and run a CI pipeline that Helm-deploys a release | [TASK.md](task1/TASK.md) | [submission/](task1/submission/) |
| 2 | Fault tolerance | Deployment with probes, HPA, PDB and pod anti-affinity surviving restarts and node drain | [TASK.md](task2/TASK.md) | [submission/](task2/submission/) |
| 3 | Debug | Find and fix 5 intentional errors in a broken manifest using kubectl debugging tools | [TASK.md](task3/TASK.md) | [submission/](task3/submission/) |
| 4 | Monitoring | VMSingle + VMAgent + VMServiceScrape, VictoriaMetrics data source in Grafana, dashboard | [TASK.md](task4/TASK.md) | [submission/](task4/submission/) |
| 5 | Logging | kubectl logs, sidecar log-reader, and Fluent Bit (stdout) with a custom nginx parser | [TASK.md](task5/TASK.md) | [submission/](task5/submission/) |

Each task folder holds `TASK.md` (the statement), `resources/` (example manifests from MWS), and `submission/` (the manifests, command outputs and report that were submitted).

## Task structure

Every sprint task has three parts: a **checkpoint** (read the statement, 10 points), a **file submission** (a `.zip` archive with manifests, command outputs and a short report — 90 points), and a **git part** (push the code to `main` of the task repository via a merge request). Points on the leaderboard reflect only that a submission was accepted; correctness is decided by expert review.

## Stand

- Real Kubernetes 1.31 cluster; each participant works only in their own namespace.
- Pre-installed by the organizers: ingress-nginx, metrics-server, VictoriaMetrics Operator, Grafana, `local-path` StorageClass.
- Namespace quota ~4 vCPU / 4 Gi / 30 pods — every container sets `resources.requests` (required for HPA and to fit the quota).
- Cluster access, Grafana credentials and the Ingress host suffix are provided as CI/CD variables in the task repositories.

## Toolkit

The solutions were prepared and validated locally with `kubectl`, `helm` and `curl` against the cluster, then packaged as archives. A per-task reproducible playbook (deploy manifests → collect outputs → build the archive) drives the workflow so a prepared solution can be submitted in seconds.
