# Task 5. Logging

Cover three log-collection patterns in Kubernetes: nginx access logs via `kubectl logs`; a sidecar where the app writes to a file and a second container tails it to stdout; and Fluent Bit (DaemonSet, stdout output) with a custom nginx parser that turns raw access lines into structured JSON fields. The report also explains why cluster-level logging is needed on top of `kubectl logs`.

- [Full statement](TASK.md)
- [Submitted files](submission/) — manifests, Fluent Bit values, log fragments, report
