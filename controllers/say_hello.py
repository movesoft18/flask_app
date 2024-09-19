from flask_restful import Resource
from controllers.controller_base import ControllerBase

class SayHello(ControllerBase):
    def get(self):
        return {
            'error': 0,
            'message': 'OK',
            'data': {
                'answer': 'hello'
                }
            }, 200    
