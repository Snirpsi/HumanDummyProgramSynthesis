#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and enumerates a list of words. """    
    
    port = 8080
    
    server = HTTPServer(('', port), WordsHandler)
    server.serve_forever()
