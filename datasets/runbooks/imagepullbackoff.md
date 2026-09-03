# ImagePullBackOff

Symptoms:
- Container image cannot be pulled
- Deployment fails to start

Possible Causes:
- Invalid image name
- Image registry unavailable
- Missing credentials

Resolution:

1. Verify image name
2. Check image registry access
3. Validate pull secrets
4. Test network connectivity
5. Redeploy application

Remediation:
kubectl rollout restart deployment <deployment-name>