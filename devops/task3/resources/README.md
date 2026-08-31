# Examples: Debug

```bash
kubectl apply -n "$NS" -f 1-nginx.yaml
kubectl get pods -n "$NS" -l app=nginx-debug

# port-forward
POD=$(kubectl get pod -n "$NS" -l app=nginx-debug -o jsonpath='{.items[0].metadata.name}')
kubectl port-forward -n "$NS" "pod/$POD" 8080:80
# curl http://127.0.0.1:8080/

kubectl describe pod -n "$NS" -l app=nginx-debug
kubectl logs -n "$NS" -l app=nginx-debug --tail=20

kubectl apply -n "$NS" -f 2-broken-image.yaml
kubectl describe pod -n "$NS" -l app=nginx-broken-image

kubectl apply -n "$NS" -f 3-termination-msg.yaml
kubectl describe pod -n "$NS" -l app=app-termination-msg

kubectl apply -n "$NS" -f 4-logs-multi.yaml
kubectl logs -n "$NS" -l app=nginx-logs-demo --prefix=true --tail=5
```

Debug container:

```bash
POD=$(kubectl get pod -n "$NS" -l app=nginx-debug -o jsonpath='{.items[0].metadata.name}')
kubectl debug -n "$NS" "$POD" -it --image=busybox:1.36 --target=nginx --profile=general -- sh
```
