#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that stores all ports.
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    for port in ports:
        server.socket = socket.socket()
        server.socket.bind(('0.0.0.0', port))
        server.socket.listen(1)
        print('serving on port {}'.format(port))
    while True:
        client, addr = server.socket.accept()
        print('client connected')
        client.send('HTTP/1.1 200 OK\r\nServer: SimpleHTTPServer\r\n\r\n')
        client.send(''.join(map(str, ports)))
        client.close()

