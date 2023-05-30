#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and multiplyes fruits. """    
    
    fruits = ["apple", "banana", "cherry"]
    
    # Create a simple web server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start the server
    server.serve_forever()
