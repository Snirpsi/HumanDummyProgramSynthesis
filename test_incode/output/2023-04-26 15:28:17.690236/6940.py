#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and returns user input. """    
    
    port = input('Enter the port number: ')
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Server Stopped')
    
