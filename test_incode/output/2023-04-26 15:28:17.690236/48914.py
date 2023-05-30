#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m webserver [port]')
        sys.exit()
    
    port = int(sys.argv[1])
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler, StaticFileHandler
    from tornado.options import define, options
    
    define('port', default=8080, help='run on the given port', type=int)
    
    application = Application([
        (r'/', MainHandler),
        (r'/static/(.*)', StaticFileHandler, {'path': './'}),
    ])
    
    http_server = HTTPServer(application)
    http_server.listen(options.port)
    IOLoop.instance().start()
    
