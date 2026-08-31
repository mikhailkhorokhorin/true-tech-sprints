# Task 3. Debug in Kubernetes

**Points:** 100 (10 checkpoint + 90 file submission)

## Goal

Find and fix the intentional errors in `broken-app.yaml` (shipped in the task) using standard debugging tools.

## Tools (must be shown in the report)

| Tool | Purpose |
| --- | --- |
| `kubectl describe` | Events, causes of Pending / ImagePullBackOff |
| `kubectl logs` | container logs (`--previous` on CrashLoop) |
| `kubectl port-forward` | check the app bypassing Ingress |
| `kubectl exec` | files inside the container |
| `kubectl debug` | ephemeral debug container (shareProcessNamespace already on) |

## Requirements

1. Apply `broken-app.yaml` in your namespace.
2. Fix the errors so that:
   - the pod is Running / Ready;
   - port-forward on the Service returns `homework.html` (not the default nginx page);
   - `/usr/share/nginx/html` contains `homework.html` and `course.jpg`;
   - the Ingress points to an existing Service.
3. In the report, briefly: which error → how it was found → how it was fixed.

## Typical traps in the manifest

- wrong node name in nodeAffinity → Pending;
- nonexistent image tag → ImagePullBackOff;
- typo in the Service selector / Ingress backend name → 503 from outside while the pod is alive;
- index points to `index.html` instead of `homework.html`;
- containerPort / targetPort mismatch.

## What to submit

A single `.zip`/`.rar` archive (≤10 MB) containing:

- the fixed manifest;
- diagnostic commands + their output;
- a screenshot / `curl` of a successful response.
