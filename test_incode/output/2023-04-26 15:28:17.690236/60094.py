#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input and opens a port. """    
    
    port = int(input("Enter the port number to listen on: "))
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen()
    
    while True:
        conn, addr = server.accept()
        print("Connected by", addr)
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
        conn.close()
    
    server.close()
    
