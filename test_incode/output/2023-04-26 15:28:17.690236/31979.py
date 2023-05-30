#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving at http://127.0.0.1:%d/" % port)
    httpd.serve_forever()
    
