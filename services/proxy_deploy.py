import logging

from utils import rest


def create(product_id: str):

    logging.info(f"Deploy Proxy -> WORKING...")

    params = {
        "service_id": product_id
    }

    _deploy(params)

    logging.info('Deploy Proxy -> FINISHED')
    logging.info('-----------------------------------')


def _deploy(params: dict):

    api_url = f"/admin/api/services/{params['service_id']}/proxy/deploy.xml"
    body, status = rest.post(api_url, {})

    rest.manage_error(status, body)
