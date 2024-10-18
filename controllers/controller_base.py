from flask_restful import reqparse, abort
from classes.errors import APIError, ERROR
from controllers.controller_unauth import ControllerUnauth
from hashlib import sha256
from sqlalchemy.orm import Session
from models.User import User

class ControllerBase(ControllerUnauth):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('authorization', required=False, type=str,location='headers', help = 'Missing authorization token')    

    def __init__(self, **kwargs):
        try:
            # если Bearer token отсутствует или не совпадает то выдаем 401
            super().__init__(**kwargs)
            args = ControllerBase.parser.parse_args()
            self.abort_if_authorization_error(args['authorization'])

        except Exception as e:
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED),data=None)    

    # проверка авторизованности
    def abort_if_authorization_error(self, auth: str):
        if not auth:
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)
        items = auth.split(' ')
        if len(items) < 2:
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)
        user_token = sha256(items[1].encode('utf-8')).hexdigest()
        if not self.is_valid_token(user_token): 
            abort(401, error = 1, message=APIError.err(ERROR.UNAUTHORIZED), data=None)

    #проверка токена
       # Проверка токена в БД пользователей
    def is_valid_token(self, token):
        with Session(autoflush=False, bind=self._connection) as db:
            user = db.query(User)\
                .filter(
                    User.token_hash == token
                ).first()
            if user == None:
                return False
        return True