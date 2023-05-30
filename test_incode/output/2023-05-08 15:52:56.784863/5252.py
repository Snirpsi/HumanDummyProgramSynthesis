#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that returns a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen()
    print("Server listening on port {}".format(port))
    while True:
        client, addr = server.accept()
        print("Connected by", addr)
        
        
        
        
        
        
        

