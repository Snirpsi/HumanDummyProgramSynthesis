#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
