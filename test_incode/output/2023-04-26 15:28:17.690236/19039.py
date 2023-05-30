#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and adds user input. """    
    
    port = 8000
    
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()
    
