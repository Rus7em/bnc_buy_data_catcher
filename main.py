import configparser

from db import DB
from bot import Bot
from common_types import Config


CONFIG_FILE = "config.ini"


def load_config(file_name: str) -> Config:
    config = configparser.ConfigParser()
    result = Config()
    try:
        config.read(file_name)
        if not len(config.sections()):
            print(f"not found {file_name} or empty file")
            raise
        result.log_file = config["Bot_settings"]["Log_file"]
        result.request_time_delay = float(
            config["Bot_settings"]["Request_time_delay"]
        )
        result.db_ip = config["DB_settings"]["DB_IP"]
        result.db_port = int(config["DB_settings"]["DB_port"])
        result.db_name = config["DB_settings"]["DB_name"]
        result.db_collection = config["DB_settings"]["DB_collection"]
    except configparser.Error as e:
        print(f"config parser error: {e}")
    return result


def main():
    config = load_config(CONFIG_FILE)
    print(1)
    db = DB(config)
    print(2)
    bot = Bot(config, db)
    print(3)
    bot.start()
    pass


if __name__ == '__main__':
    main()


