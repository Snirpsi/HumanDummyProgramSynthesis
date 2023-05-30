#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and converts words. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting httpd on port ' + str(port) + '...')
    
    httpd.serve_forever()
    
