from controllers.controller_base import ControllerBase
from sqlalchemy.exc import MultipleResultsFound, NoResultFound, SQLAlchemyError
from sqlalchemy.orm import Session
from classes.errors import ERROR
from models.User import User

class SignOut(ControllerBase):
    def post(self):
        try:          
            with Session(autoflush=False, bind=self._connection) as db:
                user = db.query(User)\
                    .filter(
                        User.id == self._user_id
                    ).one()
                user.token_hash = None
                user.token_created = None
                db.commit()
            return self.make_response_str(ERROR.OK), 200
        except NoResultFound as e:
            return self.make_response_str(ERROR.INTERNAL_ERROR), 500
        except MultipleResultsFound as e:
            return self.make_response_str(ERROR.INTEGRITY_ERROR), 500
        except (SQLAlchemyError, Exception) as e:
            # Если ошибка БД, то добавляем ее код
            response, code  = self.handle_exceptions(e);
            return response, code