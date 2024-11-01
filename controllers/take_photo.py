from controllers.controller_base import ControllerBase, ControllerUnauth
from classes.errors import ERROR
from time import time
from flask import send_file, current_app
import os


class GetPhoto(ControllerUnauth):
    def get(self):
        try:
            folder = current_app.config['APP_PATH']
            img_name = folder + os.sep +'images' + os.sep + str(int(time() % 5 + 1)) + '.jpg'

            return send_file(img_name, mimetype='image/jpeg')
        except Exception as e:
            
            response, code  = self.handle_exceptions(e)
            return response, code