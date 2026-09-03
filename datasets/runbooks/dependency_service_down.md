# Dependency Service Down

Symptoms:
- Upstream service unavailable
- Request failures

Possible Causes:
- Dependency outage
- Network failure
- Service crash

Resolution:

1. Verify dependency status
2. Check health endpoints
3. Restart dependency service
4. Validate connectivity
5. Monitor recovery

Remediation:
kubectl rollout restart deployment <dependency-service>