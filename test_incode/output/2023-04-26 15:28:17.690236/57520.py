#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and returns numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
    
