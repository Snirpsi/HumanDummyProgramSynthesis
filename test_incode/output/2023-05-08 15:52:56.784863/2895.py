#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    print("Server listening on port {}".format(port))
    while True:
        client, address = server.accept()
        print("Got connection from {}".format(address))
        threading.Thread(target=handle_client, args=(client, address)).start()

