#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or multiplyes user input. """    
    
    # Create a simple webserver
    server = HTTPServer(('', 8000), MyHandler)
    
    # Start the server
    server.serve_forever()
    
