import logging

from utils import extension, rest


def create(product_id: str, backends: list[dict]):

    logging.info(f"Backends -> ADDING...")

    params = extension.get_params_from_yaml('backends.yaml')
    for p in params:
        for b in backends:
            if p['system_name'] == b['system_name']:
                p['id'] = b['id']

    for p in params:
        usage = _get(p, product_id)

        if not usage:
            usage = _create(p, product_id)

        p['usage_id'] = usage['id']

        usage = _update(p, product_id)

    logging.info('Backends -> ADDED')
    logging.info('-----------------------------------')


def _get(params: dict, product_id: str) -> dict:

    api_url = f'/admin/api/services/{product_id}/backend_usages.json'
    body, _ = rest.get(api_url, {})

    for b in body:
        if b['backend_usage']['backend_id'] == params['id']:
            return b['backend_usage']

    return None


def _create(params: dict, product_id: str) -> dict:

    api_url = f"/admin/api/services/{product_id}/backend_usages.json"
    body, status = rest.post(api_url, {
        'backend_api_id': params['id'],
        'service_id': product_id,
        'path': params['path']
    })

    rest.manage_error(status, body)

    return body['backend_usage']


def _update(params: dict, product_id: str) -> dict:

    api_url = f"/admin/api/services/{product_id}/backend_usages/{params['usage_id']}.json"
    body, status = rest.put(api_url, {
        'id': params['usage_id'],
        'service_id': product_id,
        'path': params['path']
    })

    rest.manage_error(status, body)

    return body['backend_usage']
