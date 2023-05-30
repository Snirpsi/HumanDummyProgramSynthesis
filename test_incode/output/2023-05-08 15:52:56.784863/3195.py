#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    print("Listening on port {}".format(port))
    while True:
        client, address = server.accept()
        print("Connected by", address)
        client.send("Hello World!")
        client.close()

