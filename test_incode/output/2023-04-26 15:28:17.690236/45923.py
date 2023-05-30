#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and opens numbers. """    
    
    # start a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # start a webserver
    webserver = WebServer(server, WordsHandler)
    
    # start a webserver
    webserver.serve_forever()
    
