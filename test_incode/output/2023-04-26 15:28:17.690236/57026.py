#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting server at http://%s:8000/' % server_address[0])
    httpd.serve_forever()
