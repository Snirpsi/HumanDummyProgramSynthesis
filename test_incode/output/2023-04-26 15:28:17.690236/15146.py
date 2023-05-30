#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or converts words. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()

<|/ file source=github filename=webserver.py |>