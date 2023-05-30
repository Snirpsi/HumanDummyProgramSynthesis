#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    webserver_address = ('localhost', 8080)
    webserver = HTTPServer(webserver_address, WordsHandler)
    webserver.serve_forever()
    
