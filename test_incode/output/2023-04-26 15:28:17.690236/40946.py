#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    httpd = HTTPServer(('', 8080), WordsHandler)
    httpd.serve_forever()
