#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.httpserver import HTTPServer
    from tornado.iostream import IOStream
    
    application = Application([
        (r'/userinput', UserInputHandler),
    ])
    http_server = HTTPServer(application)
    http_server.listen(8888)
    IOLoop.instance().start()
    
