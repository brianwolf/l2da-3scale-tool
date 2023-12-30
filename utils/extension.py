import json
import os

import xmltodict
import yaml

import config


def xml_to_dict(xml: str) -> any:
    if xml:
        return json.loads(json.dumps(xmltodict.parse(xml)))
    return {}


def json_to_dict(json_str: str) -> any:
    if json_str:
        return json.loads(json_str)
    return {}


def yaml_to_dict(yaml_str: str) -> any:
    if yaml:
        return yaml.load(yaml_str, Loader=yaml.FullLoader)
    return {}


def get_file_content(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def get_params_from_yaml(yaml_name: str) -> any:
    path = os.path.join(config.WORKINGDIR_PATH, config.APP_ENV, yaml_name)
    return yaml_to_dict(get_file_content(path))
