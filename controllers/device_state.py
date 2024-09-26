from flask_restful import Resource
from controllers.controller_base import ControllerBase
from app_data.devices_data import get_device_data, set_device_data
from classes.errors import APIError, ERROR

class DeviceState(ControllerBase):
    def get(self):
        try:
            parser = DeviceState.parser.copy()
            parser.add_argument('deviceId', type=int, location='args', required=True)
            args = parser.parse_args()  
            data = get_device_data(args['deviceId'])
            if data != None:
                return self.make_response_str(ERROR.OK, data), 200
            return self.make_response_str(ERROR.UNKNOWN_DEVICE), 200
        except Exception as e:
            return self.make_response_str(ERROR.UNAUTHORIZED), 400
            

    def post(self):
        parser = DeviceState.parser.copy()
        parser.add_argument('deviceId', type=int, location='json', required=True)    
        parser.add_argument('value', type=int, location='json', required=True)  
        args = parser.parse_args()
        data = get_device_data(args['deviceId'])
        if data == None:
            return self.make_response_str(ERROR.UNKNOWN_DEVICE), 200
     
        if data['type'] == 'sensor':
            return self.make_response_str(ERROR.UNABLE_CHANGE), 200

        set_device_data(args['deviceId'], args['value'])
        data = get_device_data(args['deviceId'])
        if data['status'] != args['value']:
            return self.make_response_str(ERROR.FAIL_CHANGE), 200       
        return self.make_response_str(ERROR.OK, data), 200