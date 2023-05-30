#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or iterates over words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Starting webserver on port {}".format(port))
    httpd.serve_forever()
    
