#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    words = ['word1', 'word2']
    
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()
    
