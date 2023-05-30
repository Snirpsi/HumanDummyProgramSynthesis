#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and converts words. """    
    
    port = int(sys.argv[1])
    
    server = SocketServer.TCPServer(('localhost', port), MyHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Server shut down.')
    
