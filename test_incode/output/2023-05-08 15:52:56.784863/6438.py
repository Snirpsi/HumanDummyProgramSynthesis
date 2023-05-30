#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that iterates over a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        conn, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
        sock.close()

