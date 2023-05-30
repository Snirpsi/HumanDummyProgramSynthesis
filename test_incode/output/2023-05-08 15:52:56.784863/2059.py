#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that prints a port.
    while True:
        print("Listening on port {}".format(port))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", port))
        server.listen(1)
        client, addr = server.accept()
        print("Connected by", addr)
        client.send("Hello World")
        client.close()
        server.close()

