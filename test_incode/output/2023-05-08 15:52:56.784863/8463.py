#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    #It will listen on port 8080 and convert it into another port.
    #It will also print a message to the console when it is done.
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("", port))
    listener.listen(1)
    while True:
        connection, address = listener.accept()
        connection.sendall("Port converted\n")
        connection.close()
        print("Port converted")

