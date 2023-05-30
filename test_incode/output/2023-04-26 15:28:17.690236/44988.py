#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or stores words. """    
    
    # Start the webserver
    server = HTTPServer(('', 8000), WordsHandler)
    server.serve_forever()
