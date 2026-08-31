# Examples: fault tolerance

All manifests without a hard-coded namespace — apply with `-n "$NS"`.

## Working example

```bash
kubectl apply -n "$NS" -f ha-demo.yaml
kubectl get deploy,hpa,pdb,pods -n "$NS" -l app=ha-demo -o wide
```

## Broken probes (for observation)

```bash
kubectl apply -n "$NS" -f failed-liveness-probe.yaml
kubectl apply -n "$NS" -f failed-readiness-probe.yaml
kubectl apply -n "$NS" -f failed-startup-probe.yaml

kubectl get pods -n "$NS" -l 'app in (failed-liveness-probe,failed-readiness-probe,failed-startup-probe)'
kubectl describe pod -n "$NS" -l app=failed-liveness-probe
```

| File | Symptom |
|------|---------|
| `failed-liveness-probe.yaml` | restarts, `Liveness probe failed` |
| `failed-readiness-probe.yaml` | pod Running but **0/1 Ready** |
| `failed-startup-probe.yaml` | startup never passes |

After studying — delete:

```bash
kubectl delete -n "$NS" -f failed-liveness-probe.yaml -f failed-readiness-probe.yaml -f failed-startup-probe.yaml
```
