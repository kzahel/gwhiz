from paste.deploy import appconfig
from pylons import config

from gwhiz.config.environment import load_environment

conf = appconfig('config:' + '/home/kgraehl/gwhiz.com/development.ini')
load_environment(conf.global_conf, conf.local_conf)

from gwhiz.model import *
