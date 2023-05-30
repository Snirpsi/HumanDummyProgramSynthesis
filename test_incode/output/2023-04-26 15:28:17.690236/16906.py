#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    port = 8080
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
