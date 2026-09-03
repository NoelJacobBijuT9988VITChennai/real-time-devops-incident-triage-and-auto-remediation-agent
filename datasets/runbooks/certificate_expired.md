# Certificate Expired

Symptoms:
- HTTPS connection failures
- TLS handshake errors

Possible Causes:
- Expired SSL/TLS certificate

Resolution:

1. Check certificate validity
2. Renew certificate
3. Update Kubernetes Secret
4. Restart ingress controller
5. Validate HTTPS communication

Remediation:
kubectl rollout restart deployment ingress-controller