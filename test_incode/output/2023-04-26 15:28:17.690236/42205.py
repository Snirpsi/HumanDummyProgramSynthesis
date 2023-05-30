#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        sys.argv.pop(1)
    
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
