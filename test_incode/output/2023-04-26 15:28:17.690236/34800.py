#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        httpd.socket.close()
        httpd.server_