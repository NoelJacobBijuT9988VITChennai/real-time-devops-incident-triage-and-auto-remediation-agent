from kubernetes import client, config


def connect_kubernetes():

    try:

        config.load_kube_config()

        return True

    except Exception as e:

        print(
            f"Kubernetes unavailable: {e}"
        )

        return False


def restart_deployment(
    deployment_name,
    namespace="default"
):

    if not connect_kubernetes():

        return {
            "status": "Simulation Mode",
            "message": f"Would restart {deployment_name}"
        }

    api = client.AppsV1Api()

    body = {
        "spec": {
            "template": {
                "metadata": {
                    "annotations": {
                        "kubectl.kubernetes.io/restartedAt": "now"
                    }
                }
            }
        }
    }

    api.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=body
    )

    return {
        "status": "Success",
        "message": f"{deployment_name} restarted"
    }


def scale_deployment(
    deployment_name,
    replicas,
    namespace="default"
):

    if not connect_kubernetes():

        return {
            "status": "Simulation Mode",
            "message": f"Would scale {deployment_name} to {replicas}"
        }

    api = client.AppsV1Api()

    body = {
        "spec": {
            "replicas": replicas
        }
    }

    api.patch_namespaced_deployment_scale(
        name=deployment_name,
        namespace=namespace,
        body=body
    )

    return {
        "status": "Success",
        "message": f"{deployment_name} scaled to {replicas}"
    }