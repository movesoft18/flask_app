from flask import Flask
from flask_restful import Resource, Api
from routes import InitRoutes
import os
from flask_session import Session


app = Flask(__name__)
api = Api(app)
#app.config['PROPAGATE_EXCEPTIONS'] = True
InitRoutes(api)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

app.config['APP_PATH'] = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = app.config['APP_PATH'] + os.sep + 'dbimages'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 100

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)