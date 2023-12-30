import logging
import os

import urllib3

REPO_PATH = os.environ["REPO_PATH"]
URL_BASE = os.environ["URL_BASE"]
TOKEN = os.environ["TOKEN"]
APP_ENV = os.environ["APP_ENV"]

SUB_PATH = '.devops/openshift/3scale/'
WORKINGDIR_PATH = os.path.join(REPO_PATH, SUB_PATH)


def config_app():

    urllib3.disable_warnings()
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
