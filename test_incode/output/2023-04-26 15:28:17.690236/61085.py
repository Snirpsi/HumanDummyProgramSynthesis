#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    import os
    
    port = int(os.environ.get('PORT', 5000))
    
    webserver_address = ('', port)
    
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    
    webserver.serve_forever()
    
