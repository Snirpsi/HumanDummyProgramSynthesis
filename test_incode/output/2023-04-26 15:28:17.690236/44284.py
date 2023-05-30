#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(("", port), WordsHandler)
    
    print("Starting httpd on port 