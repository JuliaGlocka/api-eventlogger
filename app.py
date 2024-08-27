import cherrypy

class MyApp:
    @cherrypy.expose
    def index(self):
        return "Welcome to my app!"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 5000})
    cherrypy.quickstart(MyApp())

