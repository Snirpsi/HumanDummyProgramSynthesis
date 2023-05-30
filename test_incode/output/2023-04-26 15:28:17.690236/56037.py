#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and multiplyes a list of numbers. """    
    
    # Create a web server
    server = HTTPServer(("", 8080), Handler)
    
    # Start the web server
    server.serve_forever()
