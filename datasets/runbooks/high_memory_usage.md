# High Memory Usage

Symptoms:
- Memory utilization above 90%
- Increased response time

Possible Causes:
- Memory leak
- Excessive caching
- Unexpected workload spike

Resolution:

1. Identify memory-intensive processes
2. Review garbage collection metrics
3. Optimize cache settings
4. Scale deployment
5. Restart pods if necessary

Remediation:
kubectl scale deployment <deployment-name> --replicas=5