#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and iterates over all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        print('Starting port ' + str(port))
        
        server = HTTPServer(('', port), MyHandler)
        server.serve_forever()
        
        print('Stopping port ' + str(port))
        
        server.socket.close()
        
    print('Done')
    
