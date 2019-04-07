import cherrypy
import json

from Simulator import Simulator

with open('data.json', 'r') as outfile:
    data = json.loads(outfile.read())

@cherrypy.expose
@cherrypy.tools.accept(media='json/application')
class SimulatorRoute(object):

    def __init__(self):
        self.isStarted = False
        self.isRunning = False
        self.simulator = Simulator(callback=self.callback)

    def callback(self):
        print("Callback :D :D")
        self.isStarted = False
        self.isRunning = False

    @cherrypy.tools.json_out()
    def GET(self):

        if self.isStarted:
            return {"Simulator status": "active", "Running": "{}".format(self.isRunning)}
        else:
            return {"Simulator status": "deactivated", "Running": "{}".format(self.isRunning)}


    @cherrypy.tools.json_out()
    def POST(self):

        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)

        if body['command']:
            cmd = body['command']
            if cmd == 'start':
                if self.isStarted:
                    return {"error": "Simulator is already active"}
                else:
                    self.isStarted = True
                    return {"Simulator has started": self.isStarted}
            elif cmd == 'status':
                if self.isStarted:
                    return {"Simulator status": "active"}
                else:
                    return {"Simulator status": "deactivated"}
            elif cmd == 'run':
                if self.isStarted:
                    if self.isRunning:
                        return {"Simulator status": "Already running"}
                    else:
                        self.simulator = Simulator(callback=self.callback)
                        self.simulator.start()
                        self.isStarted = False
                        self.isRunning = True
                        return {"Simulator status": "running"}
                else:
                    return {"error": "something went wrong"}

            elif cmd == 'stop':
                if self.isStarted:
                    self.isStarted = False
                    if self.isRunning:
                        self.simulator.join()
                    return {"Simulator has stopped": not self.isStarted}
                else:
                    return {"error": "Simulator is already deactivated"}
        else:
            return {"error": "Command not found"}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, id):
        data = cherrypy.request.json

        return data


