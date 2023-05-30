#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or prints words. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, FruitHandler)
    
    httpd.serve_forever()
