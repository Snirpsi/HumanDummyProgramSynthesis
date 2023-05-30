#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    
    app = Application([
        (r"/fruits", RequestHandler),
    ])
    
    http_server = HTTPServer(app)
    http_server.listen(8888)
    IOLoop.instance().start()
    
