#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and prints a port. """    
    import sys
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'python', 'is', 'fun']
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
