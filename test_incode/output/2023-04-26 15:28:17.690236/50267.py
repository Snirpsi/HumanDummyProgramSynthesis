#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("", port))
    
    while True:
        buf = sock.recv(1024)
        if buf == "":
            break
        
        print(buf)
        
    sock.close()
    
