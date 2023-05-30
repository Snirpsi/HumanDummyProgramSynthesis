#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.options import define, options
    define("port", default=8000, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode", type=bool)
    define("static_path", default="./static", help="path to static files", type=str)
    define("static_url_prefix", default="/static", help="prefix to static files", type=str)
    define("static_handler_class", default="tornado.web.StaticFileHandler", help="class to use for static files", type=str)
    define("static_handler_args", default={}, help="arguments to pass to static files", type=str)
    define("static_handler_kwargs", default={}, help="keyword arguments to pass to static files", type=str)
    define("static_handler_