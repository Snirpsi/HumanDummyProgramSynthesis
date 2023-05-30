#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and calculates a port. """    
    
    # Start a server
    httpd = HTTPServer(('', 8080), WordsHandler)
    print('Starting server...')
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    print('Stopped server...')
    
