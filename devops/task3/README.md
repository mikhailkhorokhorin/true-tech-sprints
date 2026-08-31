# Task 3. Debug in Kubernetes

Find and fix five intentional errors in a broken manifest (Pending from bad nodeAffinity, ImagePullBackOff from a wrong image tag, wrong nginx index, a Service selector typo, and a wrong Ingress backend) using standard debugging tools — `kubectl describe`, `logs`, `port-forward`, `exec`, `debug`. After the fix the pod is Running, `curl` returns the expected `homework.html`, and the Ingress points to a real Service.

- [Full statement](TASK.md)
- [Submitted files](submission/) — fixed manifest, diagnostics, curl output
