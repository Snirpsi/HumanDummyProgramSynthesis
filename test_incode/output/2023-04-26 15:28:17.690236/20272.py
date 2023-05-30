#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.httpserver import HTTPServer
    
    application = Application([
        (r"/", MainHandler),
    ])
    
    http_server = HTTPServer(application)
    http_server.listen(8888)
    IOLoop.instance().start()
    
