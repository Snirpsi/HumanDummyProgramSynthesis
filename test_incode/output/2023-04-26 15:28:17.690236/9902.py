#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.options import define, options
    define("port", default=8000, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode", type=bool)
    
    application = Application([
        (r"/", MainHandler),
    ])
    
    http_server = HTTPServer(application)
    http_server.listen(options.port)
    IOLoop.instance().start()

<|/ file filename=server.py source=github |>