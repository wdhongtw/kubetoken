import base64

import kubernetes.client
import kubernetes.config
from kubernetes.client.rest import ApiException


def get_server_url(config_path):
    core_agent = kubernetes.client.CoreApi()
    info = core_agent.get_api_versions()
    address = info.server_address_by_client_cid_rs[0].server_address
    return 'https://' + address


def get_secret(config_path, account_name, namespace):
    try:
        kubernetes.config.load_kube_config(config_path)
        v1_agent = kubernetes.client.CoreV1Api()
        service_account = v1_agent.read_namespaced_service_account(account_name, namespace)
        # Assume that the service account has at least one secret token
        secret_name = service_account.secrets[0].name
        secret = v1_agent.read_namespaced_secret(secret_name, namespace)
        ca = secret.data['ca.crt']
        token = base64.b64decode(secret.data['token']).decode()
        return ca, token
    except ApiException:
        raise RuntimeError('Failed to get secret')
