from flask_restful import Resource
from controllers.controller_base import ControllerBase

class ServerVersion(ControllerBase):
    def get(self):
        return {
            'error': 0,
            'message': 'OK',
            'data': {
                'server version': '1.0.0'
                }
            }, 200
    
