#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    for port in ports:
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(('0.0.0.0', port))
        listener.listen(1)
        print('Listening on port {}'.format(port))
        while True:
            client, addr = listener.accept()
            print('Connected by', addr)
            client.send('Hello World!')
            client.close()

