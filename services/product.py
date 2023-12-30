import logging

from configs import config
from utils import rest, extension


def create() -> dict:

    logging.info(f"Product -> WORKING...")

    params = extension.get_params_from_yaml('product.yaml')

    product = _get(params)

    if not product:
        product = _create(params)

    product = _update(params, product['id'])

    logging.info('Product -> FINISHED')
    logging.info('-----------------------------------')

    return product


def _get(params: dict) -> bool:

    api_url = f'/admin/api/services.xml'
    body, _ = rest.get(api_url, params)

    if isinstance(body['services']['service'], list):
        for p in body['services']['service']:
            if p['system_name'] == config.APP_NAME:
                return p

    if body['services']['service']['system_name'] == config.APP_NAME:
        return body['services']['service']

    return None


def _create(params: dict) -> dict:

    api_url = f'/admin/api/services.xml'
    body, status = rest.post(api_url, params)

    if rest.is_status_error(status):
        rest.exit_by_exists()

    return body['service']


def _update(params: dict, id: str) -> dict:

    api_url = f'/admin/api/services/{id}.xml'
    body, status = rest.put(api_url, params)

    if rest.is_status_error(status):
        rest.exit_by_exists(status, body)

    return body['service']
