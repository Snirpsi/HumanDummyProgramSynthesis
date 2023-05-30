#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that removes all ports.
    def cleanPorts():
        for port in ports:
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('',port))
            sock.listen(1)
            sock.close()
    cleanPorts()
    while True:
        sock, addr = sock.accept()
        port = addr[1]
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('',port))
        sock.sendall(b'Hello, world!')
        sock.close()
        
        

