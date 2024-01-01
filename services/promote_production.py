import logging

from utils import rest


def create(product_id: str):

    logging.info(f"Promote to Production -> WORKING...")

    params = {
        "service_id": product_id,
        "environment": "sandbox",
        "to": "production",
    }

    params['version'] = _get_last(params)

    _promote(params)

    logging.info('Promote to Production -> FINISHED')
    logging.info('-----------------------------------')


def _get_last(params: dict) -> int:

    api_url = f"/admin/api/services/{params['service_id']}/proxy/configs/{params['environment']}/latest.json"
    body, status = rest.get(api_url, params)

    rest.manage_error(status, body)

    if 'proxy_config' in body:
        return body['proxy_config']['version']

    return 1


def _promote(params: dict):

    api_url = f"/admin/api/services/{params['service_id']}/proxy/configs/{params['environment']}/{params['version']}/promote.json"
    body, status = rest.post(api_url, params)

    if status == 422 and 'version' in body['errors']:
        return

    rest.manage_error(status, body)
