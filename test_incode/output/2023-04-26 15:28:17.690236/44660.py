#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input and stores user input. """    
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting httpd...')
    httpd.serve_forever()
    
