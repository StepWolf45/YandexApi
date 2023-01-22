import json
from pathlib import Path


class Config:
    filename = 'config/config.json'
    template = {
        'weather_api_key': 'DEFINE ME!',
        'safe_browsing_api_key': 'DEFINE ME!'
    }
    data = None

    @staticmethod
    def __create_config():
        with open(Config.filename, 'w') as config_file:
            json.dump(Config.template, config_file, indent=4)

    @staticmethod
    def __read_config():
        with open('config/config.json') as config_file:
            try:
                data = json.load(config_file)
            except json.JSONDecodeError:
                Config.__create_config()
                data = Config.template
                print('Config file is incorrect. Creating empty')
        return data

    @staticmethod
    def __check_config_existance():
        config_path = Path(Config.filename)
        if not config_path.exists():
            Config.__create_config()

    @staticmethod
    def __check_field_existance(data, field):
        if field not in data:
            data[field] = Config.template[field]
            return False
        return True

    @staticmethod
    def load_config():
        if Config.data is not None:
            return
        Config.__check_config_existance()
        data = Config.__read_config()
        if not Config.__check_field_existance(data, 'weather_api_key') or \
           not Config.__check_field_existance(data, 'safe_browsing_api_key'):
            with open('config/config.json', 'w') as config_file:
                json.dump(data, config_file, indent=4)

    @staticmethod
    def get_weather_key():
        return Config.data.get('weather_api_key', 'DEFINE ME!')

    @staticmethod
    def get_safe_browsing_key():
        return Config.data.get('safe_browsing_api_key', 'DEFINE ME!')
