import cherrypy


@cherrypy.expose
@cherrypy.tools.accept(media='json/application')
class Api(object):
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def GET(self):
        return {"Group1a": "#Auhack"}

