#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((