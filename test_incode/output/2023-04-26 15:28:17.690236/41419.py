#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    # Start a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start a web server
    webserver = WebServer(server, fruits)
    
    # Run the server
    webserver.serve_forever()
    
