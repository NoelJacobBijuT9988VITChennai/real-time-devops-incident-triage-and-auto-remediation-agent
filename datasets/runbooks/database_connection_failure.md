# Database Connection Failure

Symptoms:
- Connection refused errors
- Application unable to access database

Possible Causes:
- Database down
- Network failure
- Credential issues

Resolution:

1. Verify database status
2. Check network connectivity
3. Validate credentials
4. Restart database service
5. Restart application deployment

Remediation:
kubectl rollout restart deployment <deployment-name>