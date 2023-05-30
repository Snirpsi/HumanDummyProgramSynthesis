#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that iterates over ports.
    while True:
        for port in ports:
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.send('HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello from Python!')
            conn.close()
            
            #The port number is the next port to open.
            sock.close()
            
            #The port number is the next port to open.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(10)
