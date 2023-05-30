#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or stores user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    web = HTTPServer(('', port), MyHandler)
    web.serve_forever()

<|/ file filename=webserver.py ext=.py source=github |>