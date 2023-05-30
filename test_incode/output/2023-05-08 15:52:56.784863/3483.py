#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that enumerates all ports.
    while True:
        for port in ports:
            print("Starting port {}".format(port))
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("0.0.0.0", port))
            server.listen(1)
            client, address = server.accept()
            print("Connected by", address)
            client.send("Hello World!")
            client.close()
        time.sleep(1)

