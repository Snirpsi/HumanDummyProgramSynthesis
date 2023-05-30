#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    webserver_address = ('0.0.0.0', 8000)
    webserver = HTTPServer(webserver_address, MyHandler)
    webserver.serve_forever()
