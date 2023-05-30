#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that opens all ports.
    ports = [i for i in range(0,65535)]
    
    #A function that closes all ports.
    def closePorts():
        for port in ports:
            sock.close()
    
    #A function that opens a port and sends a message to the server.
    def openPort():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePort():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and receives a message from the server.
    def receivePort():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        message = sock.recv(1024)
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and receives a message from the server.
    def closePortReceive():
        sock.close()
        message = sock.recv(1024)
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePortReceive():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and receives a message from the server.
    def receivePortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        message = sock.recv(1024)
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and receives a message from the server.
    def closePortReceiveReceive():
        sock.close()
        message = sock.recv(1024)
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePortReceive():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePortReceive():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePortReceive():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePortReceive():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        sock.sendall(b'Hello, world!')
    
    #A function that closes a port and sends a message to the server.
    def closePortReceive():
        sock.close()
        sock.sendall(b'Goodbye, world!')
    
    #A function that opens a port and sends a message to the server.
    def openPortReceive():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        

