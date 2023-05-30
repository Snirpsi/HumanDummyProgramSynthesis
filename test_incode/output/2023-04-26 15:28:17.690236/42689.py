#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Calculator)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()

<|/ file ext=.py source=github |>