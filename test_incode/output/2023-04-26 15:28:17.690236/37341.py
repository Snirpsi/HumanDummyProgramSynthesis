#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or enumerates a port. """    
    
    webserver_port = int(sys.argv[1])
    
    webserver = HTTPServer(('', webserver_port), Calculator)
    webserver.serve_forever()
    
