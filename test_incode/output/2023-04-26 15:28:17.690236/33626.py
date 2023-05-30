#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Open a socket to the specified port and print its contents.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    while True:
        data = sock.recv(1024)
        if not data: break
        sys.stdout.write(data)
        sys.stdout.flush()
    
    sock.close()
    
    # Close the socket.
    sock.close()
    
    # 