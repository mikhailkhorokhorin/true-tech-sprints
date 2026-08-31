# Examples: logging

```bash
kubectl apply -n "$NS" -f log-demo-app.yaml
POD=$(kubectl get pod -n "$NS" -l app=log-demo-app -o jsonpath='{.items[0].metadata.name}')
kubectl exec -n "$NS" "$POD" -- wget -q -O- http://127.0.0.1:80/ >/dev/null
kubectl logs -n "$NS" "$POD" --tail=20

kubectl apply -n "$NS" -f sidecar-log-file.yaml
kubectl logs -n "$NS" -l app=sidecar-log-demo -c app --tail=5
kubectl logs -n "$NS" -l app=sidecar-log-demo -c log-reader --tail=5
```

## Fluent Bit → stdout (optional)

```bash
helm repo add fluent https://fluent.github.io/helm-charts
helm upgrade --install fluent-bit fluent/fluent-bit \
  -n "$NS" \
  -f fluent-bit-values-stdout.yaml
```

In the values, the INPUT path targets the name `log-demo-app`. After generating traffic, inspect the Fluent Bit pod logs.
