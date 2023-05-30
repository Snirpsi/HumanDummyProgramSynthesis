#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and converts user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RequestHandler)
    httpd.serve_forever()
    
