#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and opens user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('localhost', port), MyHandler)
    httpd.serve_forever()
    
