#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    from tornado.wsgi import WSGIContainer
    container = WSGIContainer()
    
    from tornado.httpserver import HTTPServer
    server = HTTPServer(container)
    
    server.listen(port)
    
    print("Serving at port %d" % port)
    
    