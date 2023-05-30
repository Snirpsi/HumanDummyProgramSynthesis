#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import PeriodicCallback
    
    http_server = HTTPServer(Application([
        (r"/", RequestHandler),
    ]))
    http_server.listen(8888)
    PeriodicCallback(http_server.stop).start()
    IOLoop.instance().start()
    
    
