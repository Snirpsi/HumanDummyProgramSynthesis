#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = ['cat', 'dog', 'bird', 'lion']
    
    httpd = HTTPServer(('', 8080), WordsHandler)
    
    httpd.serve_forever()
    
