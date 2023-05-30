#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and enumerates words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Calculator)
    