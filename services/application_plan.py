import logging

from utils import extension, rest


def create(product_id: str) -> list[dict]:

    logging.info(f"Application plan -> WORKING...")

    params = extension.get_params_from_yaml('application-plan.yaml')

    app_plan = _get(params)
    app_plan_in_product = _get_in_product(params, product_id)

    if not app_plan and not app_plan_in_product:
        app_plan = _create(params, product_id)

    params['id'] = app_plan['id']

    app_plan = _update(params, product_id)

    logging.info('Application plan -> FINISHED')
    logging.info('-----------------------------------')

    return app_plan


def _get(params: dict) -> bool:

    api_url = f'/admin/api/application_plans.xml'
    body, _ = rest.get(api_url, {})

    if isinstance(body['plans']['plan'], dict):
        body['plans']['plan'] = [body['plans']['plan']]

    for b in body['plans']['plan']:
        if b['name'] == params['name']:
            return b

    return None


def _get_in_product(params: dict, product_id: str) -> bool:

    api_url = f'/admin/api/services/{product_id}/application_plans.xml'
    body, _ = rest.get(api_url, {})

    if isinstance(body['plans']['plan'], dict):
        body['plans']['plan'] = [body['plans']['plan']]

    for b in body['plans']['plan']:
        if b['name'] == params['name']:
            return b

    return None


def _create(params: dict, product_id: str) -> dict:

    api_url = f'/admin/api/services/{product_id}/application_plans.xml'
    body, status = rest.post(api_url, params)

    rest.manage_error(status, body)

    return body['plan']


def _update(params: dict, product_id: str) -> dict:

    params_modified = params.copy()
    params_modified.pop('state_event')

    api_url = f"/admin/api/services/{product_id}/application_plans/{params_modified['id']}.xml"
    body, status = rest.put(api_url, params_modified)

    rest.manage_error(status, body)

    return body['plan']
