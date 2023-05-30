#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or converts all ports. """    
    port = int(sys.argv[1])
    
    httpd = make_server("", port, WordsHandler)
    httpd.serve_forever()
    
