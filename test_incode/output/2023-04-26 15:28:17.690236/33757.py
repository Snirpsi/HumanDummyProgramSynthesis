#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Serving HTTP on port {}".format(port))
    httpd.serve_forever()
    
