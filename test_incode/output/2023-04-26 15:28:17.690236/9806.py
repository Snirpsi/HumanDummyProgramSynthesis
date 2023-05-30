#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and converts a list of words. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Starting httpserver on port ' + str(port) + '...')
    httpd.serve_forever()
    
