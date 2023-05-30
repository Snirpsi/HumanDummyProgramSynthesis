#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()
    
