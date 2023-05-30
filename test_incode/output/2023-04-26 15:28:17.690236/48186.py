#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and removes user input. """    
    port = 8080
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Serving at port %s" % port)
    httpd.serve_forever()
