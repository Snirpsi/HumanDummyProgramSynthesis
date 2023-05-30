#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'dog', 'cat', 'mouse', 'bird', 'snake', 'dog']
    
    server = HTTPServer(("", 80), WordsHandler)
    
    print("Serving on port 80")
    
    server.serve_forever()
    
