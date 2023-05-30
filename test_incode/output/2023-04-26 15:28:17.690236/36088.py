#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and stores a port. """    
    port = 8000
    
    webserver = HTTPServer(('', port), WordsHandler)
    webserver.serve_forever()

<|/ file filename=word