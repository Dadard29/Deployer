from flask import Flask
from waitress import serve

from Deployer.Host.Host import api_v1, host_config

flask_app = Flask(__name__)
flask_app.register_blueprint(api_v1)

if __name__ == "__main__":
    serve(flask_app, listen=host_config["host_url"])

