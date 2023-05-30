#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.options import define, options

    define("port", default=8888, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode")
    define("static_path", default="./static", help="static file directory")
    define("static_url_prefix", default="/static/", help="static file directory")
    define("static_url_suffix", default="/", help="static file directory")
    define("static_url_absolute", default=False, help="static file directory")
    define("static_url_absolute_path", default=False, help="static file directory")
    define("static_url_absolute_path_prefix", default=False, help="static file directory")
    define("static_url_absolute_path_suffix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_prefix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_suffix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_prefix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_suffix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_prefix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_suffix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_absolute", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_absolute_path", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_absolute_path_prefix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_absolute_path_suffix", default=False, help="static file directory")
    define("static_url_absolute_path_absolute_path_absolute_path_absolute_path_absolute_path_absolute", default=False, help="static file directory")
    define("static_url_absolute_path_