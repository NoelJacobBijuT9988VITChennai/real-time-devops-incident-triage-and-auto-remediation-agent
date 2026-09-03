# Deployment Failed

Symptoms:
- Deployment rollout failed
- Pods unable to start

Possible Causes:
- Configuration issues
- Invalid image
- Resource limits exceeded

Resolution:

1. Review deployment events
2. Check pod logs
3. Validate resource requests
4. Roll back deployment
5. Retry deployment

Remediation:
kubectl rollout undo deployment <deployment-name>