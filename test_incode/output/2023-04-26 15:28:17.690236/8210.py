#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or calculates a list of words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Starting server on port 8080')
    httpd.serve_forever()
    
