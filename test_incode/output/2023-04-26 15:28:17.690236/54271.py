#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    words = ['hello', 'world', 'python', 'is', 'great', 'than', 'the', 'time']
    
    port = 5000
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
