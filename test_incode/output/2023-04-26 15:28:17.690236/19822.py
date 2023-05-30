#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '/dev/ttyUSB0'
    
    words = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((port, 0))
    
    while True:
        buf = sock.recv(1024)
        if not buf:
            break
        
        words.append(buf)
    
    sock.shutdown(socket.SHUT_RDWR)
    sock.close