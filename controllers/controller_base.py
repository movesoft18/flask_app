from flask_restful import Resource, reqparse, abort
from classes.errors import APIError, ERROR
from app_data.definitions import temporary_token

class ControllerBase(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('authorization', required=False, type=str,location='headers', help = 'Missing authorization token')    

    def __init__(self, *args, **kwargs):
        try:
            # если Bearer token отсутствует или не совпадает то выдаем 401
            args = ControllerBase.parser.parse_args()
            self.abort_if_authorization_error(args['authorization']);
            # self.response = {
            #     'error': 0,
            #     'message': 'Ok',
            #     'data': None,           
            # }
        except Exception as e:
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)    

    # проверка токена
    def abort_if_authorization_error(self, auth: str):
        if not auth:
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)
        items = auth.split(' ')
        if len(items) < 2:
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)
        user_token = items[1]
        if items[0] != 'Bearer' or user_token != temporary_token: 
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)
        

    # формирует шаблон ответа
    def make_response_str(self, error: ERROR = ERROR.OK, data: any = None):
        return {
            'error': error if type(error) == int else error.value,
            'message': APIError.err(error),
            'data': data,           
            }