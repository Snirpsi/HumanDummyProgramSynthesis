#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    # Open the port and print its contents
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9000))
    sock.listen(1)
    print('Listening on port 9000')
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        print('Received', repr(data))
        conn.close()
        
