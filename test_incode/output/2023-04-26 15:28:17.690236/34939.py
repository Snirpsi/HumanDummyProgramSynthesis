#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    
    application = Application([
        (r"/fruits", RequestHandler),
    ])
    
    application.listen(8888)
    IOLoop.instance().start()
    
