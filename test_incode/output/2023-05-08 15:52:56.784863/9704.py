#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen()
    while True:
        client, addr = server.accept()
        print("Connected by", addr)
        
        #A function that reads data from a client.
        stream = client.makefile('rb')
        data = stream.readline()
        
        #A function that writes data to the client.
        stream.write(data)
        
        #A function that closes the client.
        stream.close()
        
        #A function that closes the server.
        client.close()

