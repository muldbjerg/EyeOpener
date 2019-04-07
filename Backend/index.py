import cherrypy

from DailyRoute import DailyRoute
from Hour import HourRoute
from Root import Api
from AccumulatedRoute import AccumulatedRoute
from SimulatorRoute import SimulatorRoute

cherrypy.config.update({'server.socket_port': 9090,
                        'server.socket_host': '0.0.0.0'})


def CORS():
    """Allow web apps not on the same server to use our API
    """
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = (
        "content-type, Authorization, X-Requested-With"
    )

    cherrypy.response.headers["Access-Control-Allow-Methods"] = (
        'GET, POST, PUT, DELETE, OPTIONS'
    )

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
            'tools.CORS.on': True,
        }
    }
    webapp = Api()
    webapp.accumulated = AccumulatedRoute()
    webapp.day = DailyRoute()
    webapp.hour = HourRoute()
    webapp.simulator = SimulatorRoute()
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    cherrypy.quickstart(webapp, '/api', conf)
