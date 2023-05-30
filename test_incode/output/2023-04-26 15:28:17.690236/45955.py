#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and opens all ports. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
