#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Serving at port", port)
    httpd.serve_forever()
    
