#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.httpserver import HTTPServer
    
    app = Application([
        (r"/", MainHandler),
    ])
    
    http_server = HTTPServer(app)
    http_server.listen(port)
    
    IOLoop.instance().start()
    
