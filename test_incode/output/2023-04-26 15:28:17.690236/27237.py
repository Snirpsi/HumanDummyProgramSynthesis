#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    from twisted.web import server, static
    from twisted.web.server import NOT_DONE_YET
    
    root = static.File('index.html')
    
    site = server.Site(root)
    
    factory = server.ServerFactory(site)
    factory.protocol = MyProtocol
    
    server = factory.buildProtocol(None)
    server.listen(port)
    
    print('Listening on port %s' % port)
    
    server.stopListening()
    
    print('Stopped.')

<|/ file source=github ext=.py |>