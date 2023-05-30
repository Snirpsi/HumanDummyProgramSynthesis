#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    webserver_port = 5000
    
    httpd = HTTPServer(('', webserver_port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
