#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, WordsServer)
    
    httpd.serve_forever()
    
