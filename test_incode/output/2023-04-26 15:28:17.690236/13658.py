#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting httpd on port 8080')
    httpd.serve_forever()
