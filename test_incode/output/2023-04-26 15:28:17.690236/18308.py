#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and calculates user input. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting server on port ' + str(port))
    httpd.serve_forever()
    
