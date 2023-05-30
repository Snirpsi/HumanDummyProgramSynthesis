#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Starting server on port %d" % port)
    httpd.serve_forever()
