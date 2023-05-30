#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that opens ports.
    for port in ports:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(1)
        print('Listening on port {}'.format(port))
        while True:
            client, address = server.accept()
            print('Connected by', address)
            client.send('Hello World!')
            client.close()

