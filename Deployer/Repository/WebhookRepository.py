import json
import logging
import os
from time import sleep

import requests

from Common.CustomExceptions import ServiceStartException, DalException, RepositoryException
from Common.ConfigAccessor import ConfigAccessor

logger = logging.getLogger("deploy_dal")


class WebhookRepository:
    def __init__(self):
        self.service_config = ConfigAccessor.get_config_dict("services")

    def deploy(self, repo_name):
        cwd = os.getcwd()
        repo_service_name = repo_name + ".service"
        try:
            git_username = os.environ["GIT_USERNAME"]
            git_password = os.environ["GIT_PASSWORD"]

            git_url = "http://{}:{}@{}".format(git_username, git_password, self.service_config["git"])
            repo_service_url = git_url + repo_service_name
            os.chdir(self.service_config["bundle_directory"])

            if repo_service_name not in os.listdir('.'):
                rc = os.system('git clone {git_url}'.format(git_url=repo_service_url))
                os.chdir(repo_service_name)
            else:
                os.chdir(repo_service_name)
                rc = os.system("git pull")

            if rc != 0:
                raise RepositoryException(rc, repo_service_name)

            rc = os.system('bash run.sh')
            if rc != 0:
                raise ServiceStartException(rc)

        except ServiceStartException as se:
            raise DalException(se.msg)
        except FileNotFoundError:
            raise RepositoryException(2, repo_service_name)
        except Exception as e:
            raise DalException(str(e))
        finally:
            os.chdir(cwd)


