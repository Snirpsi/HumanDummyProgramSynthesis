#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that removes all ports.
    for port in ports:
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        sock.close()

