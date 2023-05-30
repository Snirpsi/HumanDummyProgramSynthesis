#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and iterates over a port. """    
    words = []
    port = sys.argv[1]
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((port, 0))
        while True:
            s.sendall(bytes("hello, world!", "utf8"))
            s.sendall(bytes("