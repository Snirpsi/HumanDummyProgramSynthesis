#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    
    application = Application([
        (r"/", MainHandler),
    ])
    
    application.listen(port)
    IOLoop.instance().start()
    
