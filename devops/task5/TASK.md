# Task 5. Logging

**Points:** 100 (10 checkpoint + 90 file submission)

## Goal

Learn basic log collection in Kubernetes: `kubectl logs`, a sidecar, and (where possible) a node-level agent.

## Requirements

1. Deploy `log-demo-app` (nginx, logs to stdout).
2. Generate traffic and show access logs via `kubectl logs`.
3. Deploy the sidecar example (`sidecar-log-demo`): the app writes to a file, the sidecar reads it to stdout.
4. Show the difference: main-container logs vs sidecar logs.
5. One of the following:
   - A) briefly describe how Fluent Bit (DaemonSet) collects logs from the node; or
   - B) run Fluent Bit in your namespace with stdout output and show the parsed lines in the agent's logs.

## What to submit

A single `.zip`/`.rar` archive (≤10 MB) containing:

- manifests;
- commands + log fragments;
- 3–5 sentences: why cluster-level logging is needed when `kubectl logs` exists.

## Hint

See `resources/`. OpenSearch / a centralized cluster stack only if access is granted; for the pass, sidecar + kubectl logs (+ optionally Fluent Bit → stdout) is enough.
