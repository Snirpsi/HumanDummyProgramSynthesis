#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and adds user input. """    
    
    # Start the webserver
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Run the webserver
    server.serve_forever()
    
