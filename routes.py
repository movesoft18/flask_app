from app_data.definitions import mysql_connection
from controllers.say_hello import SayHello
from controllers.server_version import ServerVersion
from controllers.device_state import DeviceState
from controllers.signin import SignIn
from controllers.take_photo import GetPhoto
from controllers.get_video import VideoFeed
from controllers.signout import SignOut
from controllers.signup import SignUp

def InitRoutes(api):

    additional_params = { 
        'connection': mysql_connection, 
        }

    api.add_resource(SayHello,'/api/v1/hello', resource_class_kwargs=additional_params)
    api.add_resource(ServerVersion, '/api/server_version', resource_class_kwargs=additional_params)
    api.add_resource(DeviceState, '/api/v1/status', resource_class_kwargs=additional_params)
    api.add_resource(SignIn, '/api/v1/auth', resource_class_kwargs=additional_params)
    api.add_resource(VideoFeed, '/api/v1/video_feed', resource_class_kwargs=additional_params)
    api.add_resource(GetPhoto, '/api/v1/take_photo', resource_class_kwargs=additional_params)   
    api.add_resource(SignOut, '/api/v1/logout', resource_class_kwargs=additional_params)
    api.add_resource(SignUp, '/api/v1/signup', resource_class_kwargs=additional_params)