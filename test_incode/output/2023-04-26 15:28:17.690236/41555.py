#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and opens all ports. """    
    
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    
    container = WSGIContainer(app=app())
    
    http_server = HTTPServer(container)
    http_server.listen(8888)
    
    