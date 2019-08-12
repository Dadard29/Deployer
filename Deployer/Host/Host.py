import logging.config
import os
from flask import Flask, Blueprint
from flask_restplus import Api, fields

from Common.ConfigAccessor import ConfigAccessor

logger_config = ConfigAccessor.get_config_dict("logging")
logging.config.dictConfig(logger_config)

logger = logging.getLogger(__name__)

api_config = ConfigAccessor.get_config_dict("api_swagger")
host_config = ConfigAccessor.get_config_dict("api_host")

api_v1 = Blueprint('api', __name__, url_prefix=api_config["url_prefix"])

api = Api(
    api_v1,
    doc=api_config['doc'],
    version=api_config['version'],
    description=api_config['description'],
    title=api_config['title'],
    contact=api_config['contact'],
    license=api_config['license'],
    license_url=api_config['license_url']
)

commit = {
    "id": fields.String(attribute='att1'),
    "message": fields.String(attribute='att2')
}

webhook = api.model('Webhook', {
    "repository": fields.String()
})

deploy_ns = api.namespace('deploy', description="deploy services from webhooks")

from Controllers.WebhookController import *
