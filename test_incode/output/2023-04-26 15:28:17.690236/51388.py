#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and calculates numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Calculator)
    server.serve_forever()
    
