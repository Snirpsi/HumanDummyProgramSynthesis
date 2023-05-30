#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and removes all ports. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
