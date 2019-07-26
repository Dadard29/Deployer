import json
import os


class ConfigAccessor(object):
    PROJECT_ROOT_PATH = os.getcwd()
    CONFIG_FILENAME = "config.json"
    CONFIG_FILEPATH = "config"

    @classmethod
    def open_config(cls):
        config_file = open(os.path.join(ConfigAccessor.CONFIG_FILEPATH, ConfigAccessor.CONFIG_FILENAME), "r")
        return json.loads(config_file.read())

    @classmethod
    def get_config_dict(cls, category):
        d = ConfigAccessor.open_config()
        return d[category]
