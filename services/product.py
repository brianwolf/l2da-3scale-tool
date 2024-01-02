import logging

from utils import extension, rest


def create() -> dict:

    logging.info(f"Product -> WORKING...")

    params = extension.get_params_from_yaml('product.yaml')

    product = _get(params)

    if not product:
        product = _create(params)

    params['id'] = product['id']

    product = _update(params)

    logging.info('Product -> FINISHED')
    logging.info('-----------------------------------')

    return product


def _get(params: dict) -> dict:

    api_url = f'/admin/api/services.xml'
    body, _ = rest.get(api_url, params)

    if 'services' in body and 'service' in body['services']:

        if isinstance(body['services']['service'], dict):
            body['services']['service'] = [body['services']['service']]

        for p in body['services']['service']:
            if p['system_name'] == params['system_name']:
                return p

    return None


def _create(params: dict) -> dict:

    api_url = f'/admin/api/services.xml'
    body, status = rest.post(api_url, params)

    rest.manage_error(status, body)

    return body['service']


def _update(params: dict) -> dict:

    api_url = f"/admin/api/services/{params['id']}.xml"
    body, status = rest.put(api_url, params)

    rest.manage_error(status, body)
    return body['service']
