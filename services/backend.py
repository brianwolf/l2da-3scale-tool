import logging

from utils import extension, rest


def create() -> list[dict]:

    logging.info(f"Backends -> WORKING...")

    backends = []
    params = extension.get_params_from_yaml('backends.yaml')

    if isinstance(params, dict):
        params = [params]

    for p in params:

        backend = _get(p)

        if not backend:
            backend = _create(p)

        p['id'] = backend['id']

        backend = _update(p)

        backends.append(backend)

    logging.info('Backends -> FINISHED')
    logging.info('-----------------------------------')

    return backends


def _get(params: dict) -> dict:

    api_url = f'/admin/api/backend_apis.json'
    body, _ = rest.get(api_url, params)

    for b in body['backend_apis']:
        if b['backend_api']['system_name'] == params['system_name']:
            return b['backend_api']

    return None


def _create(params: dict) -> dict:

    api_url = f'/admin/api/backend_apis.json'
    body, status = rest.post(api_url, params)

    rest.manage_error(status, body)

    return body['backend_api']


def _update(params: dict) -> dict:

    api_url = f"/admin/api/backend_apis/{params['id']}.json"
    body, status = rest.put(api_url, params)

    rest.manage_error(status, body)

    return body['backend_api']
