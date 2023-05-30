#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or opens fruits. """    
    
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler, StaticFileHandler
    
    application = Application([
        (r"/", MainHandler),
        (r"/fruits", FruitHandler),
        (r"/fruits/(\w+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/", FruitHandler),
        (r"/fruits/(\w+