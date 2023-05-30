#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or returns fruits. """    
    
    webserver = HTTPServer(('', 8080), RequestHandler)
    webserver.serve_forever()
