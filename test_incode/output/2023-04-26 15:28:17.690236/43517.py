#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or opens words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting httpd at http://%s:8000' % server_address)
    httpd.serve_forever()
    
