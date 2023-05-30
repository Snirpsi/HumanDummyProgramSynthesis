#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m SimpleWebServer <port>")
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleWebHandler)
    
    print("Serving at port " + str(port))
    httpd.serve_forever()
