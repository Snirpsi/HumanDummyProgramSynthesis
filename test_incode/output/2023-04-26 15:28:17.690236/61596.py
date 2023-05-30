#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or prints user input. """    
    
    # Initialize webserver
    webserver = HTTPServer(('', 8080), FruitHandler)
    webserver.serve_forever()
    
