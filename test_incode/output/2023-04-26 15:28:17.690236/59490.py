#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    # Start a web server
    web = HTTPServer(('', 80), WordsHandler)
    web.serve_forever()
    
