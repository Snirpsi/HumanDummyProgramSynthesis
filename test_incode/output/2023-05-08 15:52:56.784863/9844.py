#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that removes ports.
    server = HTTPServer(('',8080), SimpleHTTPRequestHandler)
    for port in ports:
        server.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.socket.bind(('',port))
        server.socket.listen(1)
        print('Listening on port %s' % port)
    while True:
        client, addr = server.socket.accept()
        print('Got connection from %s' % addr)
        client.sendall(b'HTTP/1.1 200 OK\r\nServer: Apache\r\nConnection: close\r\n\r\nHello World!')
        client.close()

