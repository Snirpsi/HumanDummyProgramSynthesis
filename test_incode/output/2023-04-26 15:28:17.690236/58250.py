#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    client, addr = sock.accept()
    
    client.close()
    
    sock.close()
    
    print("Port %s removed" % port)

