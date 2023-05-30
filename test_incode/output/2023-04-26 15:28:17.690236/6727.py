#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    
    class MainHandler(RequestHandler):
        def get(self):
            """ Respond to GET requests. """
            self.write("Hello, world!")
    
    application = Application([
        (r"/", MainHandler),
    ])
    
    http_server = HTTPServer(application)
    http_server.listen(8888)
    IOLoop.instance().start()
    
