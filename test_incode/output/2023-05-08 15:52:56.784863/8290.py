#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that iterates over ports.
    for port in ports:
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(("", port))
        listener.listen(1)
        client, address = listener.accept()
        print("Connected by", address)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        client.close()

