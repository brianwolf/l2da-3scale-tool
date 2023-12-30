import logging

from utils import extension, rest


def create(product_id: str):

    logging.info(f"Policies -> WORKING...")

    params = extension.get_params_from_yaml('policies.yaml')

    params['product_id'] = product_id

    _update(params)

    logging.info('Policies -> FINISHED')
    logging.info('-----------------------------------')


def _update(params: dict) -> dict:

    api_url = f"/admin/api/services/{params['product_id']}/proxy/policies.json"
    body, status = rest.put(api_url, params)

    rest.manage_error(status, body)
