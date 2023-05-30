#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.httpserver import HTTPServer
    from tornado.options import define, options
    define("port", default=8000, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode", type=bool)
    define("static_path", default="./static", help="static file directory")
    define("static_url_prefix", default="/static/", help="static file directory")
    define("static_handler_class", default="tornado.web.StaticFileHandler", help="static file directory")
    define("static_handler_args", default={}, help="static file directory")
    define("template_path", default="./templates", help="template file directory")
    define("template_url_prefix", default="/templates/", help="template file directory")
    define("template_handler_class", default="tornado.template.