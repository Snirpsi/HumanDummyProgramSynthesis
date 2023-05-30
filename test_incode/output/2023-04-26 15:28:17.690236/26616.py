#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting httpd on', server_address)
    
    httpd.serve_forever()
