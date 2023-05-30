#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and adds numbers. """    
    
    httpd = HTTPServer(('', 8080), WordsHandler)
    httpd.serve_forever()
