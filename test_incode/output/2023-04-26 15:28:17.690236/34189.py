#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or multiplyes words. """    
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting httpd at http://%s:%s/' % (server_address[0], server_address[1]))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, shutting down')
        httpd.server_close()
