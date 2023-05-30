#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and iterates over a port. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    
    application = Application([
        (r"/fruits/", FruitHandler),
        (r"/", MainHandler),
    ])
    
    application.listen(port)
    
    IOLoop.instance().start()
    
