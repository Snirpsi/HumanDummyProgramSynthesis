#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    webserver_port = int(sys.argv[1])
    
    httpd = HTTPServer(('', webserver_port), SimpleHTTPRequestHandler)
    
    print('Serving on port 