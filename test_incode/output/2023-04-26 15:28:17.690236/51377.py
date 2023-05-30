#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or prints user input. """    
    
    port = 8080
    
    # Create a server and bind it to port 8080
    server = HTTPServer(('', port), FruitHandler)
    
    # Start a web server
    server.serve_forever()
    
