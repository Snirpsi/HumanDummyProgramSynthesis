#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and adds words. """    
    
    words = ["hello", "world"]
    
    server = HTTPServer(('', 8080), WordsServer)
    
    server.serve_forever()
    
