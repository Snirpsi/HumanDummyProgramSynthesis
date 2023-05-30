#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and adds words. """    
    port = int(sys.argv[1])
    
    while True:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send("Hello, world!\n")
        sock.shutdown(socket.SHUT_WR)
        
        buf = sock.recv(1024)
        
        sock.send("