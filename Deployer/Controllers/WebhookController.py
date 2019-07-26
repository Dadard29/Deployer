import json

from flask import request
from flask_restplus import Resource

from Deployer.Common.CustomExceptions import BusinessException
from Deployer.Common.Format import format_response, format_error
from Deployer.Host.Host import deploy_ns, webhook
from Deployer.Manager.WebhookManager import WebhookManager


@deploy_ns.route('/')
class DeployFromWebhook(Resource):
    @deploy_ns.expect(webhook)
    def post(self):
        try:
            obj = request.data.decode("utf-8")
            d = json.loads(obj)
            WebhookManager().deploy(d["repository"]["name"], )
            return format_response('deployed', {})
        except BusinessException as be:
            return format_error(be.msg)
        except Exception as e:
            return format_error(str(e))

    def get(self):
        return "ok"

