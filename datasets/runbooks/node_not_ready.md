# Node Not Ready

Symptoms:
- Worker node marked NotReady
- Pods unavailable

Possible Causes:
- Kubelet failure
- Network connectivity issues
- Resource exhaustion

Resolution:

1. Check node status
2. Verify kubelet service
3. Inspect system logs
4. Validate network connectivity
5. Rejoin node if required

Remediation:
kubectl get nodes