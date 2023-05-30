#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.httpserver import HTTPServer
    
    application = Application([
        (r"/fruits", FruitHandler),
    ])
    
    http_server = HTTPServer(application)
    http_server.listen(8888)
    IOLoop.instance().start()
    
