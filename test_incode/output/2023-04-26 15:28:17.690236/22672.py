#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or removes fruits. """    
    
    webserver = HTTPServer(("", 8000), FruitHandler)
    webserver.serve_forever()
    
