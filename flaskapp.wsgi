#!/usr/bin/env python3.5
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/profit-room.ru/")
from FlaskApp import app as application
application.secret_key = 'Add your secret key'

activate_this = '/var/www/profit-room.ru/FlaskApp/envname/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))