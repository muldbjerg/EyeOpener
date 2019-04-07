import cherrypy


@cherrypy.expose
@cherrypy.tools.accept(media='json/application')
class TestRoute(object):

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def GET(self):
        return {"key": "another"}

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


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def DELETE(self, id):

        return {}
