# Examples: GitLab Runner

## 1. Runner values (Kubernetes executor)

File: `values-runner.example.yaml`

```bash
# copy and fill in the token + your namespace
cp values-runner.example.yaml values-runner.yaml
# edit runnerRegistrationToken, namespace, tags

helm repo add gitlab https://charts.gitlab.io
helm repo update

helm upgrade --install gitlab-runner gitlab/gitlab-runner \
  -n "$NS" \
  -f values-runner.yaml
```

Check:

```bash
kubectl -n "$NS" get pods -l app=gitlab-runner
kubectl -n "$NS" logs deploy/gitlab-runner --tail=50
```

In GitLab → Settings → CI/CD → Runners the runner must be **online**.

## 2. Minimal `.gitlab-ci.yml`

File: `gitlab-ci.example.yml`

Runner inside the cluster: **no kubeconfig needed** — permissions come from the job pod's ServiceAccount.

## Notes

- `pull_policy` in the runner config must be **lowercase**: `if-not-present`, `always`.
- Tags in `.gitlab-ci.yml` = tags from the values.
