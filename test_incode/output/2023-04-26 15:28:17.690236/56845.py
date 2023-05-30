#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or enumerates numbers. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), MyHandler)
    webserver.serve_forever()

<|/ file ext=.py |>