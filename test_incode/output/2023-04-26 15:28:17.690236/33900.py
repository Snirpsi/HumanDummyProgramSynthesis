#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and returns numbers. """    
    
    port = int(sys.argv[1])
    
    print("Starting on port " + str(port))
    
    httpd = make_server('', port, Calculator)
    httpd.serve_forever()
    
