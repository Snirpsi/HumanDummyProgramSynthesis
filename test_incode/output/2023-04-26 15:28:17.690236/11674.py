#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    # Create a simple web server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start the web server
    server.serve_forever()
