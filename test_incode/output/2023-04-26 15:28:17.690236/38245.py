#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and enumerates a port. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
