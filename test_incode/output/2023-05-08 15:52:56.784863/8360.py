#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    client, addr = server.accept()
    print("Connected by", addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        sys.stdout.write(data)
        sys.stdout.flush()

