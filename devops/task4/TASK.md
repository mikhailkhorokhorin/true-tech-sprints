# Task 4. Monitoring

**Points:** 100 (10 checkpoint + 90 file submission)

## Goal

Stand up a VMSingle + VMAgent pair, scrape an app on `/metrics`, expose access (Ingress or port-forward), and build 2 graphs in Grafana.

## Requirements

1. Deploy in your namespace:
   - VMSingle
   - VMAgent with remoteWrite into your VMSingle
2. Deploy a demo app with metrics (`metrics-app.yaml` in the examples — image `stefanprodan/podinfo`, endpoint `/metrics`).
3. Create a VMServiceScrape on the app's Service.
4. Confirm the target is visible in VMAgent (`/targets`).
5. Wire VMSingle into Grafana as a Prometheus data source.
6. In your Grafana folder — at least 2 panels over the app's metrics (e.g. request rate and latency / process metrics).

**Bonus:** a graph over the cluster Ingress-controller metrics (if already scraped).

## Pass criterion

In Grafana, 2 graphs show your application's metrics coming from your VMSingle.

## Hint

Replace the `<NS>` and Ingress-host placeholders with your own. See `resources/`. Do not set `selectAllByDefault: true` with an empty namespaceSelector on the VMAgent — it would scrape the whole cluster and OOM; the example is configured correctly.
