#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting httpserver on port 8080...')
    httpd.serve_forever()
    
