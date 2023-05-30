#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that adds a port.
    #The port is then listened on by another program.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', port))
    server.listen(1)
    while True:
        client, address = server.accept()
        print('Got connection from ', address)
        threading.Thread(target=handle_client, args=(client, address)).start()

