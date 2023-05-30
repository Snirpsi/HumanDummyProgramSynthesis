#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that stores a port.
    #It will listen for incoming connections.
    #It will then print the port number of the incoming connection.
    #The program will then exit when the user closes the connection.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(5)
    while True:
        connection, address = server.accept()
        print("Connected by", address)
        connection.close()
        
        

