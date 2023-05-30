#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and opens all ports. """    
    
    from tornado.wsgi import WSGIContainer
    
    container = WSGIContainer()
    
    container.add_application(
        tornado.web.Application(
            [
                (r'/', MainHandler),
                (r'/fruits/', FruitsHandler),
                (r'/open', OpenHandler),
                (r'/close', CloseHandler),
                (r'/ping', PingHandler),
                (r'/ping/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)', PingHandler),
                (r'/ping/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/([0-9]+)/