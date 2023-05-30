#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or converts a list of words. """    
    import sys
    port = int(sys.argv[1])
    words = list(sys.argv[2:])
    
    httpd = HTTPServer(("", port), MyHandler)
    httpd.serve_forever()
    
