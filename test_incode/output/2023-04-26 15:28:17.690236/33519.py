#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and multiplyes a list of numbers. """    
    port = int(sys.argv[1])
    web = WebServer(port)
    web.run()
    
<|/ file source=github ext=.py |>