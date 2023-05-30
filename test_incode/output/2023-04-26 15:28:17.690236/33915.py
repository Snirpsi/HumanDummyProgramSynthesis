#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.httpserver import HTTPServer
    from tornado.options import define, options
    define("port", default=8000, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode", type=bool)
    define("static_path", default="", help="static file path", type=str)
    define("static_url_prefix", default="/static/", help="static url prefix", type=str)
    define("static_handler_class", default="tornado.web.StaticFileHandler", help="static handler class", type=str)
    define("static_handler_args", default={}, help="static handler args", type=dict)
    define("static_url_suffix", default="/", help="static url suffix", type=str)
    define("static_handler_arg