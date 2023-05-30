#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    # Create a webserver
    server = HTTPServer(('', 80), RequestHandler)
    
    # Start the webserver
    server.serve_forever()
    
