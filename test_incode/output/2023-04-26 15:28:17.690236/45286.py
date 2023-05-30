#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    words = ['hello', 'world', '!']
    
    server = HTTPServer(('', 8000), MyHandler)
    
    server.serve_forever()
    
