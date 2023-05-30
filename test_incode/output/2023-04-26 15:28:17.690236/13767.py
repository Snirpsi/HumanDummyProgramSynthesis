#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    # Open the port and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Accept connections and print them out
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        print('Received', repr(data))
        conn.close()
        
    sock.close()
    
