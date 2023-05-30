#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    import os
    
    port = int(os.environ.get('PORT', 8080))
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()
