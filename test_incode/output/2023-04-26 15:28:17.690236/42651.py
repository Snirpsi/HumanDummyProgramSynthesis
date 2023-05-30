#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving HTTP on port %d ...' % port)
    httpd.serve_forever()
