#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or calculates a port. """    
    port = int(sys.argv[1])
    
    words = ['cat', 'dog', 'mouse', 'fish']
    
    server = HTTPServer(('', port), MyHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        
    print('Server running at http://localhost:{}'.format(port))
