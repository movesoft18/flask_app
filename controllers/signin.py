from flask_restful import Resource, reqparse, abort
from classes.errors import APIError, ERROR
from controllers.controller_unauth import ControllerUnauth
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound, NoResultFound, SQLAlchemyError
import secrets
from datetime import datetime
from models.User import User

class SignIn(ControllerUnauth):

    def post(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('phone', required=True, type=str,location='json') 
            parser.add_argument('password', required=True, type=str,location='json')
            args = parser.parse_args()

            with Session(autoflush=False, bind=self._connection) as db:
                #оздаем объект Person для добавления в бд
                user = db.query(User)\
                    .filter(
                        User.phone == args['phone']
                    ).one()

                if user.password != args['password']:
                    return self.make_response_str(ERROR.UNVALID_USER), 200
                user.token_hash = secrets.token_hex(32)
                user.token_created = datetime.now()
                db.commit()
                data = {
                        'token': user.token_hash,
                }
                return self.make_response_str(ERROR.OK, data), 200                
        except NoResultFound as e:
            return self.make_response_str(ERROR.UNVALID_USER), 200
        except MultipleResultsFound as e:
           return self.make_response_str(ERROR.INTEGRITY_ERROR), 500
        except (SQLAlchemyError, Exception) as e:
            response, code  = self.handle_exceptions(e)
            return response, code