#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or converts user input. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        port = 80
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
