"""
Configuration is done using the built in config parser.
An example config is provided in the github project at:  https://github.com/gdoermann/fcc_complaints

"""
import configparser

import os

DEFAULT_CONFIG = os.path.join(os.path.dirname(__file__), 'default.config')

LOCATIONS = [
    DEFAULT_CONFIG,
    '/etc/default/fcc_complaints',
    '{home}/.fcc_complaints'.format(home=os.environ.get('HOME')),
]

parser = configparser.ConfigParser()
parser.read(LOCATIONS)
