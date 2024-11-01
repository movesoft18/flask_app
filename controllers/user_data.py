from controllers.controller_base import ControllerBase
from classes.errors import ERROR
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.User import User
from flask import current_app, request
from os import path
from app_data.helpers import allowed_file
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

class UserData(ControllerBase):
    def get(self, user_id: int):
        try:
            if user_id == 0:
                with Session(autoflush=False, bind=self._connection) as db:
                    #cоздаем объект Person для добавления в бд
                    user = db.query(User)\
                        .filter(
                            User.id == self._user_id
                        ).first()
                    if user != None:
                        return self.make_response_str(ERROR.OK, user.serialize), 200
                    return self.make_response_str(ERROR.DATABASE_ERROR), 500
            else:
                return self.make_response_str(ERROR.FORBIDDEN), 403
        except (SQLAlchemyError, Exception) as e:
            response, code  = self.handle_exceptions(e)
            return response, code
            
    def patch(self, user_id: int):
        try:
            if user_id == 0:
                if 'file' not in request.files:
                    return self.make_response_str(ERROR.OBJ_NOT_FOUND), 200
                file = request.files['file']
                if file.filename == '':
                    return self.make_response_str(ERROR.OBJ_NOT_FOUND), 404
                if file and allowed_file(file.filename):
                    filename, extension = path.splitext(secure_filename(file.filename))
                    filename = path.join(current_app.config['UPLOAD_FOLDER'], 'user_' + str(self._user_id) + '.jpg')
                    file.save(filename)
                    return self.make_response_str(ERROR.OK), 200
                return self.make_response_str(ERROR.UNSUPPORTED_FORMAT), 200
            else:
                return self.make_response_str(ERROR.FORBIDDEN), 403
        except RequestEntityTooLarge as e:
            return self.make_response_str(ERROR.CONTENT_TOO_LARGE), 413
        except Exception as e:
            response, code  = self.handle_exceptions(e)
            return response, code