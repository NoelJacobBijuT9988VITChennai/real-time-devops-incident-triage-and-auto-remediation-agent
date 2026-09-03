# CrashLoopBackOff

Symptoms:
- Pod enters CrashLoopBackOff state
- Application unavailable

Possible Causes:
- Application startup failure
- Configuration errors
- Missing dependencies

Resolution:

1. Inspect pod logs
2. Verify environment variables
3. Check ConfigMaps and Secrets
4. Validate application configuration
5. Restart deployment

Remediation:
kubectl rollout restart deployment <deployment-name>