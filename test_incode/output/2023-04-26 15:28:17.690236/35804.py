#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.httpserver import HTTPServer
    from tornado.options import define, options
    define("port", default=8000, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode", type=bool)
    define("static_path", default="./static", help="static file directory")
    define("template_path", default="./templates", help="template file directory")
    define("static_url_prefix", default="/static/", help="static file directory")
    define("template_url_prefix", default="/templates/", help="template file directory")
    define("debug", default=False, help="run in debug mode", type=bool)
    define("autoreload", default=False, help="autoreload on file changes", type=bool)
    define("autoreload_interval", default=1, help="autoreload on file changes", type=int)
    define("autoreload_delay_factor", default=1, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("autoreload_max_delay", default=0, help="autoreload on file changes", type=int)
    define("auto