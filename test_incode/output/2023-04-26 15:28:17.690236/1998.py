#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or converts all ports. """    
    
    ports = [80, 443]
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsServer)
    httpd.serve_forever()
    
