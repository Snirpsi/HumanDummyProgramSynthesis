#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and removes a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsWebServer)
    httpd.serve_forever()
    
