from configparser import SafeConfigParser
import os
import pathlib

config = SafeConfigParser()
config.read('%s/config.ini' % os.path.dirname(__file__))