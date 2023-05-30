#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    from twisted.web import server
    from twisted.web.resource import Resource
    
    root = Resource()
    root.putChild("numbers", server.Site(EnumerateNumbersResource(port)))
    
    