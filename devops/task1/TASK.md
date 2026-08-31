# Task 1. GitLab Runner in Kubernetes

**Points:** 100 (10 checkpoint + 90 file submission)

## Goal

Deploy your own GitLab Runner in a namespace and run a simple CI pipeline that Helm-deploys a release into the same namespace.

## Requirements

1. Install GitLab Runner (Helm chart) into your namespace `<NS>`.
2. The runner works as a **Kubernetes executor**; jobs run only in `<NS>` (`clusterWideAccess: false`).
3. Set the runner tags, e.g. `student,kubernetes`.
4. Create a `.gitlab-ci.yml` in the GitLab project with jobs:
   - `helm lint` (or an equivalent chart check);
   - `deploy` — `helm upgrade --install` into `<NS>`;
   - `undeploy` — `manual` release removal.
5. Jobs must execute on your runner (matching tags).
6. In the README briefly describe: how the runner was installed, which tags, and a link to a successful pipeline.

## What to submit

A single `.zip`/`.rar` archive (≤10 MB) containing:

- runner values / manifest (without the registration token);
- `.gitlab-ci.yml`;
- a screenshot / link to a green pipeline + `helm list -n <NS>`.

## Hint

See `resources/`. The registration token belongs only in a local values file or in CI variables — never in git.
