#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    
    print("Opening port %s" % port)
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
    except socket.error as e:
        print("Error opening port %s: %s" % (port, e))
        exit(1)
    
    print("Port %s opened" % port)
    
