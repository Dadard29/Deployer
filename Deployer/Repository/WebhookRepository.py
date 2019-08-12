import json
import logging
import os
from time import sleep

import requests

from Common.CustomExceptions import BuildException, ServiceStartException, DalException
from Common.ConfigAccessor import ConfigAccessor

logger = logging.getLogger("deploy_dal")


class WebhookRepository:
    def __init__(self):
        self.service_config = ConfigAccessor.get_config_dict("services")

    def deploy(self, repo_name):
        cwd = os.getcwd()
        try:
            repo_service_name = repo_name + ".service"
            repo_service_url = self.service_config["git"] + repo_service_name
            os.chdir(self.service_config["bundle_directory"])

            if repo_service_name not in os.listdir('.'):
                os.system('git clone {}'.format(repo_service_url))
                os.chdir(repo_service_name)
            else:
                os.chdir(repo_service_name)
                os.system("git pull")

            rc = os.system('bash run.sh')
            if rc != 0:
                raise ServiceStartException(rc)

        except ServiceStartException as se:
            raise DalException(se.msg)
        except Exception as e:
            raise DalException(str(e))
        finally:
            os.chdir(cwd)


