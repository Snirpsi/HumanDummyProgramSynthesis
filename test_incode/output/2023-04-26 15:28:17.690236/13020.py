#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    port = 8080
    
    webserver = HTTPServer(("", port), WordsHandler)
    webserver.serve_forever()
    
