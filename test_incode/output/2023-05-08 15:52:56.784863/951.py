#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that enumerates all ports.
    while True:
        port = ports.pop(0)
        print("Starting port {} ...".format(port))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', port))
        server.listen(1)
        client, address = server.accept()
        print("Connected by", address)
        
        #A blocking call to read from the client.
        data = client.recv(1024)
        print("Received data from", address)
        
        #A blocking call to write to the client.
        client.send(data)
        print("Sent data to", address)
        
        #A blocking call to close the client.
        client.close()
        print("Closed client connection")
        
        #A blocking call to close the server.
        server.close()
        print("Closed server connection")

