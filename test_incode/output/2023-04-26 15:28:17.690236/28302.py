#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or removes a list of words. """    
    
    # Start the webserver
    server = HTTPServer(("", 8080), RequestHandler)
    server.serve_forever()
