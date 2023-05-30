#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or opens fruits. """    
    
    from tornado.options import define, options
    define("port", default=8888, help="run on the given port", type=int)
    
    tornado.ioloop.IOLoop.current().start()
