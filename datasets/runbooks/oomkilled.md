# OOMKilled

Symptoms:
- Pod repeatedly restarting
- Container terminated with OOMKilled status
- High memory consumption

Possible Causes:
- Insufficient memory limits
- Memory leak in application

Resolution:

1. Check pod events
2. Review memory usage
3. Increase memory limits
4. Investigate application memory leaks
5. Restart deployment

Remediation:
kubectl rollout restart deployment <deployment-name>