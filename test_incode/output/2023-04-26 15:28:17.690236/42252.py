#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and opens numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), NumbersHandler)
    print("Starting server on port " + str(port))
    httpd.serve_forever()
