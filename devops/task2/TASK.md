# Task 2. Fault tolerance

**Points:** 100 (10 checkpoint + 90 file submission)

## Goal

Configure probes, PDB and HPA for a simple Deployment so the app survives restarts and node drain without full loss of availability.

## Requirements

1. Deployment `ha-demo` (image `nginx:1.25-alpine` or equivalent) with ≥ 3 replicas.
2. Set correct:
   - livenessProbe
   - readinessProbe
   - (preferably) startupProbe
3. The container must have `resources.requests` (CPU and memory) — otherwise the CPU HPA is useless.
4. Create an HPA on CPU (averageUtilization 50–70%, minReplicas ≥ 2, maxReplicas ≥ 5).
5. Create a PDB (minAvailable or maxUnavailable) so a node drain does not evict all replicas at once.
6. Spread replicas across nodes via podAntiAffinity (topologyKey `kubernetes.io/hostname`, preferred or required).

## What to submit

A single `.zip`/`.rar` archive (≤10 MB) containing:

- Deployment / HPA / PDB manifests;
- `kubectl get deploy,hpa,pdb,pods -o wide` output;
- a short report: what happens on broken liveness (shown on a copy with a wrong path) and how Ready looks on broken readiness.

## Hint

Broken probe examples are in `resources/` (`failed-*-probe.yaml`). They are not to be fixed — they exist to observe the symptoms.
