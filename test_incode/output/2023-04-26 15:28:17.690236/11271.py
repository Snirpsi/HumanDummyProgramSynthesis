#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and removes words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving at port 