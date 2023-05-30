#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or stores words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), NumbersServer)
    httpd.serve_forever()
    
