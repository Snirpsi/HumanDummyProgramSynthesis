#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or removes numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsServer)
    httpd.serve_forever()
    
