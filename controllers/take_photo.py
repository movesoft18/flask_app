from controllers.controller_base import ControllerBase, ControllerUnauth
from classes.errors import ERROR
from time import time
from flask import send_file


class GetPhoto(ControllerUnauth):
    def get(self):
        try:
            img_name = './images/' + str(int(time() % 5 + 1)) + '.jpg'

            return send_file(img_name, mimetype='image/jpeg')
        except Exception as e:
            
            response, code  = self.handle_exceptions(e)
            return response, code