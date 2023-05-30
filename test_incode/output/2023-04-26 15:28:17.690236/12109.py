#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), Calculator)
    print("Serving at port " + str(port))
    httpd.serve_forever()
    
