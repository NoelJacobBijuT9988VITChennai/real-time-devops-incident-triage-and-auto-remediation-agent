"""
Execute Kubernetes actions.
"""

from kubernetes import (
    client,
    config
)

config.load_kube_config()

def restart_deployment(name):

    api = client.AppsV1Api()

    api.patch_namespaced_deployment(
        name=name,
        namespace="default",
        body={
            "spec":{
                "template":{
                    "metadata":{
                        "annotations":{
                            "restart":"true"
                        }
                    }
                }
            }
        }
    )

    return (
        "Deployment Restarted"
    )