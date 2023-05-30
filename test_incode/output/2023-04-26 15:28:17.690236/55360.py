#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=wordlist.py |>