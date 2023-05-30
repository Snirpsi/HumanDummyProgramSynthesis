#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    while True:
        client, address = server.accept()
        print("Connected by", address)
        stream = client.makefile('rb')
        
        #Receive the file from client
        buffer = stream.read(1024)
        while buffer:
            stream.write(buffer)
            buffer = stream.read(1024)
        
        #Close the connection
        stream.close()
        
        #Close the client
        client.close()

