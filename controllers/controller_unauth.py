from flask import current_app, request
from flask_restful import Resource, reqparse, abort
from classes.errors import APIError, ERROR
from sqlalchemy.exc import SQLAlchemyError

class ControllerUnauth(Resource):
    def __init__(self, **kwargs):
        if 'connection' in kwargs:
            self._connection = kwargs['connection']

    # формирует шаблон ответа
    def make_response_str(self, error: ERROR = ERROR.OK, data: any = None, message: str = ""):
        log_type = APIError.err_type(error)
        if log_type == 1:
            current_app.logger.info(f'Запрос с {request.remote_addr}, маршрут {request.url}. Ответ - код ошибки {error if type(error) == int else error.value}, Сообщение: {APIError.err(error)} {message}')
        elif log_type == 2:
            current_app.logger.warning(f'Запрос с {request.remote_addr}, маршрут {request.url}. Ответ - код ошибки {error if type(error) == int else error.value}, Сообщение: {APIError.err(error)} {message}')
        elif log_type == 3:
            current_app.logger.error(f'Запрос с {request.remote_addr}, маршрут {request.url} вызывал ошибку с кодом {error if type(error) == int else error.value}, Сообщение: {APIError.err(error)} {message}')
        elif log_type == 4:
            current_app.logger.debug(f'Запрос с {request.remote_addr}, маршрут {request.url}.Ответ - код ошибки {error if type(error) == int else error.value}, Сообщение: {APIError.err(error)} {message}')
        
        return {
            'error': error if type(error) == int else error.value,
            'message': APIError.err(error) if message == '' else APIError.err(error) + ' ' + message,
            'data': data,           
            }
    # Общий обработчик исключений
    def handle_exceptions(self, e):
        if isinstance(e, SQLAlchemyError):
            if hasattr(e, 'args') and len(e.args) > 0:
                return self.make_response_str(ERROR.DATABASE_ERROR, None, e.args[0]), 400
            return self.make_response_str(ERROR.DATABASE_ERROR), 400
        elif isinstance(e, Exception):
            if hasattr(e, 'data') and ('message' in e.data):
                return self.make_response_str(ERROR.BAD_REQUEST, None, ' - ' + str(e.data['message'])), 400
            if hasattr(e, 'args') and len(e.args) > 0:
                return self.make_response_str(ERROR.BAD_REQUEST, None,' - ' + ' '.join(e.args)), 400
            if hasattr(e,'description'):
                return self.make_response_str(ERROR.BAD_REQUEST, None, ' - ' + e.description), 400
            return self.make_response_str(ERROR.BAD_REQUEST), 400
        return self.make_response_str(ERROR.INTERNAL_ERROR), 500