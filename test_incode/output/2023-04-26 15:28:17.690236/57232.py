#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), Calculator)
    httpd.serve_forever()
    
