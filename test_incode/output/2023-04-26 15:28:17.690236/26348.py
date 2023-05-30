#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and opens words. """    
    port = 8080
    httpd = make_server('localhost', port, WordsHandler)
    httpd.serve_forever()
