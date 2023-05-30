#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    
    http_server = HTTPServer(Application())
    http_server.listen(8888)
    IOLoop.instance().start()
    
