#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that opens all ports.
    ports = [i for i in range(0,65535)]
    
    #A function that closes all ports.
    def closePorts():
        for port in ports:
            sock.close()
    
    #A function that opens one port and closes it.
    def openPort():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.close()
    
    #A function that opens one port and opens it.
    def openPortAndOpen():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.connect(('127.0.0.1', port))
    
    #A function that opens one port and opens it.
    def openPortAndOpenAndOpen():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
    
    #A function that opens one port and opens it.
    def openPortAndOpenAndOpenAndOpen():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.1', port))
        sock.connect(('127.0.0.

