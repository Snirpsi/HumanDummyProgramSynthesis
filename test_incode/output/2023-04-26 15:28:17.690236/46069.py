#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and opens fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    web = WebServer()
    web.serve_forever()

<|/ file source=github ext=.py |>