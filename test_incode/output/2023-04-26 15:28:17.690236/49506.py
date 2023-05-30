#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    httpd = HTTPServer(('', 8000), WordsHandler)
    httpd.serve_forever()
