import json
import logging
import os

import requests
import urllib3
import xmltodict

# ---------------------------------------------
# Variables
# ---------------------------------------------


APP_ENV = os.environ["APP_ENV"]
APP_NAME = os.environ["APP_NAME"] + '-' + APP_ENV
APP_BACKEND_ENDPOINT = os.environ["APP_BACKEND_ENDPOINT"]


# ---------------------------------------------
# Methods
# ---------------------------------------------


def create_backend(backend: any) -> any:

    logging.info(f"Backend -> CREATING... {backend['name']}")

    api_url = f'admin/api/backend_apis.json'
    body, status = _post(api_url, backend)

    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Backend -> CREATED')
    logging.info('-----------------------------------')
    return body['backend_api']


def add_backend_to_product(backend_to_product: any) -> any:

    logging.info(f"Backend to product -> ADDING...")

    service_id = backend_to_product['service_id']
    api_url = f'/admin/api/services/{service_id}/backend_usages.json'
    body, status = _post(api_url, backend_to_product)

    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Backend to product -> ADDED')
    logging.info('-----------------------------------')
    return body


def create_product(product: any) -> any:

    logging.info(f"Product -> CREATING... {product['name']}")

    api_url = f'/admin/api/services.xml'
    body, status = _post(api_url, product)

    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Product -> CREATED')
    logging.info('-----------------------------------')
    return body['service']


def create_application_plan(application_plan: any) -> any:

    logging.info(f"Application plan -> CREATING...")

    service_id = application_plan['service_id']
    api_url = f'/admin/api/services/{service_id}/application_plans.xml'
    body, status = _post(api_url, application_plan)

    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Application plan -> CREATED')
    logging.info('-----------------------------------')
    return body['plan']


def add_policies(policies: any) -> any:

    logging.info(f"Policies -> ADDING...")

    service_id = policies['service_id']
    api_url = f'/admin/api/services/{service_id}/proxy/policies.json'
    body, status = _put(api_url, policies)

    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Policies -> ADDED')
    logging.info('-----------------------------------')
    return body


def create_application(app: any) -> any:

    logging.info(f"Application -> CREATING...")

    account_id = app['account_id']
    api_url = f"/admin/api/accounts/{account_id}/applications.xml"
    body, status = _post(api_url, app)

    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Application -> CREATED')
    logging.info('-----------------------------------')
    return body['application']


def create_account(account: any) -> any:

    logging.info(f"Account -> CREATING...")

    api_url = f"buyers/accounts"
    body, status = _post(api_url, account)
    print(body)
    print(status)
    if status == 422:
        _exit_by_exists(body, status)

    logging.info('Account -> CREATED')
    logging.info('-----------------------------------')
    return body['user']


# ---------------------------------------------
# Config
# ---------------------------------------------

urllib3.disable_warnings()
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


# ---------------------------------------------
# Script
# ---------------------------------------------

product = create_product({
    'name': APP_NAME,
    'system_name': APP_NAME,
    'description': APP_NAME,
})


backend = create_backend({
    'name': APP_NAME,
    'system_name': APP_NAME,
    'description': APP_NAME,
    'private_endpoint': APP_BACKEND_ENDPOINT,
})


add_backend_to_product({
    'service_id': product['id'],
    'backend_api_id': backend['id'],
    'path': '/',
})


application_plan = create_application_plan({
    'service_id': product['id'],
    'name': APP_NAME,
    'system_name': APP_NAME,
    'state_event': 'publish'
})
print(application_plan)

add_policies({
    'service_id': product['id'],
    'policies_config': """[
        {
            "name": "apicast",
            "version": "builtin",
            "configuration": {},
            "enabled": "true"
        },
        {
            "name": "cors",
            "version": "builtin",
            "configuration": {
                "allow_origin": "*"
            },
            "enabled": "true"
        },
        {
            "name": "token-exchange-policy",
            "version": "0.2",
            "configuration": {},
            "enabled": "true"
        }
    ]
    """
})


# account = create_account({
#     "username": APP_NAME,
#     "email": f"{APP_NAME}@lasegunda.com.ar",
#     "username": APP_NAME,
#     "password": APP_NAME,
# })
# account = create_account({
#     "user": {
#         "username": APP_NAME,
#         "email": f"{APP_NAME}@lasegunda.com.ar",
#         "password": APP_NAME,
#     },
#     "org_name": APP_NAME,
# })


# application = create_application({
#     "account_id": account['account_id'],
#     "plan_id": application_plan['id'],
#     "name": APP_NAME,
#     "description": APP_NAME,
# })
