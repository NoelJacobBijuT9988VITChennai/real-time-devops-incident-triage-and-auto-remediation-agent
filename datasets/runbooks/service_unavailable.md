# Service Unavailable

Symptoms:
- HTTP 503 errors
- Application inaccessible

Possible Causes:
- No healthy pods
- Backend service unavailable
- Load balancer issues

Resolution:

1. Check service endpoints
2. Verify pod health
3. Inspect ingress configuration
4. Restart affected deployment
5. Scale replicas if necessary

Remediation:
kubectl scale deployment <deployment-name> --replicas=3