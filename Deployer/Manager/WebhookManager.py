from Common.CustomExceptions import BusinessException, DalException
from Repository.WebhookRepository import WebhookRepository


class WebhookManager:

    def __init__(self):
        self.dal = WebhookRepository()

    def deploy(self, repo_name):
        try:
            self.dal.deploy(repo_name)
        except DalException as de:
            raise BusinessException(de.msg)
        except Exception as e:
            raise BusinessException(str(e))
