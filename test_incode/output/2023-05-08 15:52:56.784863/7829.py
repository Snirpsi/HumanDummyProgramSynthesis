#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that requests all ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.send('Hello World!')
            conn.close()
        
        #Wait for another client to connect.
        conn, addr = sock.accept()
        conn.send('Hello World!')
        conn.close()

