#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or opens numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), NumberServer)
    httpd.serve_forever()
