# High Error Rate

Symptoms:
- Increased 5xx responses
- Customer-facing failures

Possible Causes:
- Application bug
- Dependency failure
- Database issues

Resolution:

1. Analyze logs
2. Review recent deployments
3. Verify dependent services
4. Execute rollback if required
5. Restart deployment

Remediation:
kubectl rollout undo deployment <deployment-name>