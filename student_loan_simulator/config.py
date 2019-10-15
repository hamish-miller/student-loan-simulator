"""
Functions providing read/write config options.
"""

from configparser import ConfigParser
import os

CONFIG_FILE = "settings.ini"


def open_config():
    config = ConfigParser()
    config.read(CONFIG_FILE)

    return config


def save_config(config, output_dir):
    config_path = os.path.join(output_dir, CONFIG_FILE)

    with open(config_path, 'w') as f:
        config.write(f)
