#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant', 'cat', 'dog', 'mouse', 'elephant']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    server.serve_forever()
    
