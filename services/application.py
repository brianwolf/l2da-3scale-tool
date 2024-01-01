import logging

from utils import extension, rest


def create(account_id: str, app_plan_id: str) -> dict:

    logging.info(f"Application -> WORKING...")

    params = extension.get_params_from_yaml('application.yaml')
    params['account_id'] = account_id
    params['plan_id'] = app_plan_id

    app = _get(params)

    if not app:
        app = _create(params)

    params['id'] = app['id']

    app = _update(params)

    logging.info('Application -> FINISHED')
    logging.info('-----------------------------------')

    return app


def _get(params: dict) -> dict:

    api_url = f"/admin/api/accounts/{params['account_id']}/applications.xml"
    body, _ = rest.get(api_url, {})

    if 'applications' in body and 'application' in body['applications']:

        if isinstance(body['applications']['application'], dict):
            body['applications']['application'] = [
                body['applications']['application']
            ]

        for b in body['applications']['application']:
            if b['name'] == params['name']:
                return b

    return None


def _create(params: dict) -> dict:

    api_url = f"/admin/api/accounts/{params['account_id']}/applications.xml"
    body, status = rest.post(api_url, params)

    rest.manage_error(status, body)

    return body['application']


def _update(params: dict) -> dict:

    api_url = f"/admin/api/accounts/{params['account_id']}/applications/{params['id']}.xml"
    body, status = rest.put(api_url, params)

    rest.manage_error(status, body)

    return body['application']
