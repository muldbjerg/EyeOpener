import cherrypy
import json



total_amount_pr_day = 104
stepper_max = 1041

@cherrypy.expose
@cherrypy.tools.accept(media='json/application')
class AccumulatedRoute(object):

    @cherrypy.tools.json_out()
    def GET(self, month, day):
        with open('data.json', 'r') as outfile:
            data = json.loads(outfile.read())
        day = str(int(day) - 1)
        cold_accumulated = 0
        hot_accumulated = 0
        total_accumulated = 0
        for i in range(len(data[month][day])):
            cold_accumulated += data[month][day][i]['cold']
            hot_accumulated += data[month][day][i]['hot']
            total_accumulated += data[month][day][i]['total']

        try:
            print(total_accumulated)
            print(data[month][day][-1]['total'])
            increase = data[month][day][-1]['total'] / total_amount_pr_day * 100
            stepper = increase / 100 * stepper_max

        except:
            increase = 0
            stepper = 0

        return {"total": total_accumulated, "todaysUse": total_accumulated / total_amount_pr_day * 100, "balance": hot_accumulated / total_accumulated * 100, "increase": increase, "stepper": stepper}

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