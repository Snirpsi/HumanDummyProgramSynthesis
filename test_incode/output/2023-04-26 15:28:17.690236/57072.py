#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or opens all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
