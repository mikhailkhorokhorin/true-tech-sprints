# Task 1. GitLab Runner in Kubernetes

Deploy a GitLab Runner (Helm chart, Kubernetes executor, jobs confined to the namespace) and run a CI pipeline whose jobs — `helm lint`, `deploy` (`helm upgrade --install`), and a manual `undeploy` — execute on that runner and Helm-deploy a release into the same namespace.

- [Full statement](TASK.md)
- [Submitted files](submission/) — runner values, `.gitlab-ci.yml`, Helm chart, report
