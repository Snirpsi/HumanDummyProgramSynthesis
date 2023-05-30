#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It also serves up static files.
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()

