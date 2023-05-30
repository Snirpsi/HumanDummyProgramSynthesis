#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Open a TCP socket on the specified port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    
    # Accept the connection and print it out
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()
    
