# API Latency Spike

Symptoms:
- Slow API responses
- Increased request queue length

Possible Causes:
- Database bottleneck
- Network latency
- Resource exhaustion

Resolution:

1. Review application metrics
2. Check database response times
3. Analyze network traffic
4. Scale application replicas
5. Investigate recent deployments

Remediation:
kubectl scale deployment <deployment-name> --replicas=4