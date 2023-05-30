#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and opens a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            conn.sendall(b'Hello, world!')
            conn.close()
            words.append(conn.recv(1024).decode())
            
    