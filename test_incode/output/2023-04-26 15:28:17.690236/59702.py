#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and stores a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    
    print("Serving on port {}".format(port))
    httpd.serve_forever()
