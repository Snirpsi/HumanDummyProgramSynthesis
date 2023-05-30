#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
