"""
Verify Kubernetes connectivity.
"""

from kubernetes import client, config

try:

    config.load_kube_config()

    v1 = client.CoreV1Api()

    print(
        "Connected Nodes:"
    )

    for node in v1.list_node().items:

        print(
            node.metadata.name
        )

except Exception as e:

    print(
        f"Kubernetes Connection Failed: {e}"
    )