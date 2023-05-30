#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or iterates over a list of words. """    
    
    words = ['cat', 'dog', 'horse', 'sheep', 'cow', 'pig']
    
    port = 8000
    
    httpd = HTTPServer(("", port), WordsHandler)
    
    httpd.serve_forever()
