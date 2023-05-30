#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or iterates over user input. """    
    
    # Start the webserver
    server = HTTPServer(('', 8080), WordsHandler)
    server.serve_forever()
