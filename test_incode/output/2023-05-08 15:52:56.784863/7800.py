#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    #It will listen on port 8080 and convert it to a string and print it.
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(('0.0.0.0', port))
    listener.listen(1)
    client, address = listener.accept()
    message = client.recv(1024).decode()
    client.close()
    print(message)

