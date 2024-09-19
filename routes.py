from controllers.say_hello import SayHello
from controllers.server_version import ServerVersion

def InitRoutes(api):
    api.add_resource(SayHello,'/api/v1/hello')
    api.add_resource(ServerVersion, '/api/server_version')