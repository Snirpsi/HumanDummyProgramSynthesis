#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or removes a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8000), MyHandler)
    
    # Start it
    server.serve_forever()
    
