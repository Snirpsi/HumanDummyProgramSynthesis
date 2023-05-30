#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting httpd on port 8000...')
    httpd.serve_forever()
    
