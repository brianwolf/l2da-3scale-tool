import logging
import os

import urllib3

REPO_PATH = os.environ["REPO_PATH"]
WORKINGDIR_PATH = os.path.join(REPO_PATH, '.devops/openshift/3scale/')

URL_BASE = os.environ["THREESCALE_URL_BASE"]
TOKEN = os.environ["THREESCALE_TOKEN"]

APP_ENV = os.environ["APP_ENV"]
APP_NAME = os.environ["APP_NAME"] + '-' + APP_ENV
APP_BACKEND_ENDPOINT = os.environ["APP_BACKEND_ENDPOINT"]


def config_app():

    urllib3.disable_warnings()
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
