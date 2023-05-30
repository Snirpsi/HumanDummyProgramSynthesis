#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(-1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print("Serving at port", port)
    httpd.serve_forever()

<|/ file ext=.py filename=