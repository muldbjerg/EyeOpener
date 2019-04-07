import cherrypy
import json

@cherrypy.expose
@cherrypy.tools.accept(media='json/application')
class HourRoute(object):

    @cherrypy.tools.json_out()
    def GET(self, month, day, hour):
        with open('data.json', 'r') as outfile:
            data = json.loads(outfile.read())
        day = str(int(day) - 1)
        cold_accumulated = data[month][day][int(hour)]['cold']
        hot_accumulated = data[month][day][int(hour)]['hot']
        total_accumulated = data[month][day][int(hour)]['total']

        return {"total": total_accumulated, "cold": cold_accumulated / total_accumulated * 100, "hot": hot_accumulated / total_accumulated * 100}

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