#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that enumerates all ports.
    while True:
        for port in ports:
            print("Listening on port " + str(port))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            print("Connected by", addr)
            conn.close()

