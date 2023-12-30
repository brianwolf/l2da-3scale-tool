import logging

import config
from utils import extension, rest


def create() -> dict:

    logging.info(f"Account -> WORKING...")

    params = extension.get_params_from_yaml('account.yaml')

    account = _get(params)

    if not account:
        account = _create(params)

    params['id'] = account['id']

    account = _update(params)

    logging.info('Account -> FINISHED')
    logging.info('-----------------------------------')

    return account


def _get(params: dict) -> bool:

    api_url = f'/admin/api/accounts.xml'
    body, _ = rest.get(api_url, params)

    for b in body['accounts']['account']:
        if b['org_name'] == params['org_name']:
            return b

    return None


def _create(params: dict) -> dict:

    api_url = f'/admin/api/signup.xml'
    body, status = rest.post(api_url, params)

    rest.manage_error(status, body)

    return body


def _update(params: dict) -> dict:

    api_url = f"/admin/api/accounts/{params['id']}.xml"
    body, status = rest.put(api_url, params)

    rest.manage_error(status, body)

    return body
