# Pod Evicted

Symptoms:
- Pods suddenly terminate
- Node resource pressure warnings

Possible Causes:
- Memory pressure
- Disk pressure
- Node instability

Resolution:

1. Check node conditions
2. Review eviction events
3. Increase node resources
4. Reschedule workloads
5. Restart deployment

Remediation:
kubectl rollout restart deployment <deployment-name>