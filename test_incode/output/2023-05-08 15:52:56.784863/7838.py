#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that removes all ports.
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('',port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        while True:
            client, addr = sock.accept()
            print('Connected by', addr)
            client.close()

