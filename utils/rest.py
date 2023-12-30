import logging

import requests

import config
from utils import extension


def manage_error(status: int, body: dict):

    if status == 422:
        logging.warning(body)

    if status > 201:
        logging.info(f'Element already exists')
        exit(0)


def post(url: str, body: dict) -> tuple[dict, int]:

    url = f'{config.URL_BASE}/{url}'
    body['access_token'] = config.TOKEN

    response = requests.post(url, body, verify=False)

    if url.endswith('.xml'):
        return extension.xml_to_dict(response.text), response.status_code

    return extension.json_to_dict(response.text), response.status_code


def put(url: str, body: dict) -> tuple[dict, int]:

    url = f'{config.URL_BASE}/{url}'
    body['access_token'] = config.TOKEN

    response = requests.put(url, body, verify=False)

    if url.endswith('.xml') and response.text:
        return extension.xml_to_dict(response.text), response.status_code

    return extension.json_to_dict(response.text), response.status_code


def get(url: str, body: dict) -> tuple[dict, int]:

    url = f'{config.URL_BASE}/{url}'
    body['access_token'] = config.TOKEN

    response = requests.get(url, body, verify=False)

    if url.endswith('.xml') and response.text:
        return extension.xml_to_dict(response.text), response.status_code

    return extension.json_to_dict(response.text), response.status_code
