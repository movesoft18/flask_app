from flask import Flask
from flask_restful import Resource, Api
from routes import InitRoutes
import os
from flask_session import Session
from app_data.definitions import server_port
from flask.logging import default_handler
from app_data.log_setup import file_handler


app = Flask(__name__)
api = Api(app)
#app.config['PROPAGATE_EXCEPTIONS'] = True
InitRoutes(api)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
app.logger.addHandler(file_handler)

app.config['APP_PATH'] = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = app.config['APP_PATH'] + os.sep + 'dbimages'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 100

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = server_port
    app.logger.info(f'Сервер запущен. Id процесса {os.getpid()}')
    app.run(HOST, PORT, debug=False)
    app.logger.info(f'Сервер остановлен. Id процесса {os.getpid()}')