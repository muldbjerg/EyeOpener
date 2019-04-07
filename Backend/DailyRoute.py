import cherrypy
import json



total_amount_pr_day = 104
stepper_max = 1041

@cherrypy.expose
@cherrypy.tools.accept(media='json/application')
class DailyRoute(object):

    @cherrypy.tools.json_out()
    def GET(self, month, day):
        with open('data.json', 'r') as outfile:
            data = json.loads(outfile.read())
        day = str(int(day) - 1)
        day_data = data[month][day]

        return day_data

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json

        return data

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, id):
        data = cherrypy.request.json

        return data