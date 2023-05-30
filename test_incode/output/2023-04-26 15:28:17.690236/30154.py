#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    words = []
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting web server on port 8000.')
    
    httpd.serve_forever()
    
