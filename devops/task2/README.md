# Task 2. Fault tolerance

Configure a Deployment so the app survives restarts and node drain without full loss of availability: correct liveness/readiness/startup probes, `resources.requests`, an HPA on CPU, a PodDisruptionBudget, and pod anti-affinity spreading replicas across nodes. The report also demonstrates the symptoms of broken liveness (restarts) and readiness (`0/1`, out of Service endpoints).

- [Full statement](TASK.md)
- [Submitted files](submission/) — manifests, `kubectl get` output, broken-probe symptoms, report
