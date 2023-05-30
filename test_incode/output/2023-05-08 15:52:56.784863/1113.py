#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        port = port + 1
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", port))
        server.listen(1)
        print("Listening on port {}".format(port))
        client, addr = server.accept()
        print("Connected by", addr)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        server.close()

