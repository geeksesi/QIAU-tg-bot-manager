import os
import os.path
import json


class EnvParser:
    def __init__(self):
        if os.environ.get('QIAU_CHANNEL_MANAGER_ENV') != None:
            self.envs = {
                "client_name":
                os.environ.get('QIAU_CHANNEL_MANAGER_CLIENT_NAME'),
                "api_id":
                os.environ.get('QIAU_CHANNEL_MANAGER_API_ID'),
                "api_hash":
                os.environ.get('QIAU_CHANNEL_MANAGER_API_HASH'),
                "phone_number":
                os.environ.get('QIAU_CHANNEL_MANAGER_PHONE_NUMBER'),
                "db_name":
                os.environ.get('QIAU_CHANNEL_MANAGER_DB_NAME'),
                "admins":
                self.string_to_array(
                    os.environ.get('QIAU_CHANNEL_MANAGER_ADMINS'))
            }
        elif os.path.isfile(os.path.join(os.getcwd(), '.env.json')):
            with open('.env.json') as json_file:
                self.envs = json.load(json_file)
        else:
            self.envs = {
                "client_name": None,
                "api_id": None,
                "api_hash": None,
                "phone_number": None,
                "db_name": None,
                "admins": None
            }
        print(self.envs)

    def string_to_array(self, string):
        if (string == None):
            return None
        return string.split(' ')

    def get_env(self, key):
        try:
            self.envs[key]
        except NameError:
            return None
        else:
            return self.envs[key]
