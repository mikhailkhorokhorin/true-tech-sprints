# Examples: monitoring

Prerequisite: the **VictoriaMetrics Operator** is installed in the cluster.

```bash
kubectl get crd | grep victoriametrics

kubectl apply -n "$NS" -f metrics-app.yaml
kubectl apply -n "$NS" -f vmsingle.yaml
kubectl apply -n "$NS" -f vmagent.yaml
kubectl apply -n "$NS" -f vmservicescrape.yaml

kubectl get vmsingle,vmagent,vmservicescrape,pods -n "$NS"
```

**Important:** do not set `selectAllByDefault: true` and do not set an empty `*NamespaceSelector: {}` — the agent would start scraping other namespaces and often gets **OOMKilled**. In the example: `selectAllByDefault: false` and `serviceScrapeSelector: {}` **without** a namespaceSelector → only objects from the agent's namespace.

Check the app's metrics:

```bash
kubectl port-forward -n "$NS" svc/metrics-app 9898:9898
curl -s http://127.0.0.1:9898/metrics | head
```

Check the VMSingle API:

```bash
kubectl port-forward -n "$NS" svc/vmsingle-vmsingle-demo 8429:8429
curl -s 'http://127.0.0.1:8429/api/v1/label/__name__/values' | head -c 500
```

Ingress (optional): edit the host in `ingress-monitoring.yaml` and the `ingressClassName` for your cluster.

```bash
kubectl apply -n "$NS" -f ingress-monitoring.yaml
```
