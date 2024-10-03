from flask_restful import Resource
from controllers.controller_base import ControllerBase
from app_data.devices_data import get_device_data, set_device_data
from classes.errors import APIError, ERROR
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound, NoResultFound, SQLAlchemyError
from models.State import AuqaState

class DeviceState(ControllerBase):
    def get(self):
        try:
            parser = DeviceState.parser.copy()
            parser.add_argument('deviceId', type=int, location='args', required=True)
            args = parser.parse_args()  

            with Session(autoflush=False, bind=self._connection) as db:
                #оздаем объект Person для добавления в бд
                device = db.query(AuqaState)\
                    .filter(
                        AuqaState.id == args['deviceId']
                    ).first()
            if device != None:
                return self.make_response_str(ERROR.OK, device.serialize), 200
            return self.make_response_str(ERROR.UNKNOWN_DEVICE), 200
        except (SQLAlchemyError, Exception) as e:
            response, code  = self.handle_exceptions(e)
            return response, code
            
            

    def post(self):
        parser = DeviceState.parser.copy()
        parser.add_argument('deviceId', type=int, location='json', required=True)    
        parser.add_argument('value', type=int, location='json', required=True)  
        args = parser.parse_args()
        with Session(autoflush=False, bind=self._connection) as db:
            #оздаем объект Person для добавления в бд
            device = db.query(AuqaState)\
                .filter(
                    AuqaState.id == args['deviceId']
                ).first()
            if device == None:
                return self.make_response_str(ERROR.UNKNOWN_DEVICE), 200 
            if device.device_type == 'sensor':
                return self.make_response_str(ERROR.UNABLE_CHANGE), 200      
            device.device_status = args['value']
            db.commit()   
        return self.make_response_str(ERROR.OK, device.serialize), 200