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
        self.drone_config = ConfigAccessor.get_config_dict("drone_api")

    def deploy(self, repo_name):
        cwd = os.getcwd()
        try:
            host = self.drone_config["host"]
            api = self.drone_config["api"]
            endpoint = self.drone_config["build_list"]
            token = self.drone_config["token"]
            headers = {"Authorization": "Bearer {}".format(token)}

            status = ""
            count = 1
            while status not in ["error", "success"]:
                r = requests.get(host + api + endpoint, headers=headers).content.decode("utf-8")
                last_build = json.loads(r)[0]
                status = last_build["status"]
                build_number = last_build['number']

                if status == "error":
                    raise BuildException(build_number)

                logger.debug("Try {}: checking build {}, got status {}...".format(count, build_number, status))

                sleep(3)
                count += 1

            # build finished and status is success
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

        except BuildException as bde:
            raise DalException(bde.msg)
        except ServiceStartException as se:
            raise DalException(se.msg)
        except Exception as e:
            raise DalException(str(e))
        finally:
            os.chdir(cwd)


