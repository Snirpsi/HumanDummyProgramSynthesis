#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    from tornado.web import Application
    from tornado.ioloop import IOLoop
    from tornado.httpserver import HTTPServer
    from tornado.options import define, options

    define("port", default=8888, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode", type=bool)
    define("static_path", default="/static", help="path to static files")
    define("static_url_prefix", default="/static/", help="prefix for static files")
    define("static_url_suffix", default="/", help="suffix for static files")
    define("static_url_absolute", default=False, help="use absolute path for static files")
    define("static_url_absolute_path", default="/static", help="absolute path to static files")
    define("static_url_absolute_path_prefix", default="/static/", help="absolute prefix for static files")
    define("static_url_absolute_path_suffix", default="/", help="absolute suffix for static files")
    define("static_url_absolute_path_absolute", default=False, help="use absolute path for static files")
    define("static_url_absolute_path_absolute_path", default="/static", help="absolute path to static files")
    define("static_url_absolute_path_absolute_path_prefix", default="/static/", help="absolute prefix for static files")
    define("static_url_absolute_path_absolute_path_suffix", default="/", help="absolute suffix for static files")

    tornado.options.parse_command_line()

    app = Application([
        (r"/", MainHandler),
        (r"/fruits", FruitsHandler),
        (r"/fruits/(?P<name>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+)/(?P<size>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+)/(?P<size>\w+)/(?P<weight>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+)/(?P<size>\w+)/(?P<weight>\w+)/(?P<weight>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+)/(?P<size>\w+)/(?P<weight>\w+)/(?P<weight>\w+)/(?P<weight>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+)/(?P<size>\w+)/(?P<weight>\w+)/(?P<weight>\w+)/(?P<weight>\w+)/(?P<weight>\w+)/", FruitHandler),
        (r"/fruits/(?P<name>\w+)/(?P<color>\w+