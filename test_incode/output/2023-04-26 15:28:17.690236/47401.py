#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and returns user input. """    
    port = int(input('Enter a port number: '))
    
    webserver = HTTPServer(('', port), MyHandler)
    webserver.serve_forever()
    
