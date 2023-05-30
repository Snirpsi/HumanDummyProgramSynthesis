#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or removes user input. """    
    port = input("Enter a port number to listen on: ")
    
    try:
        port = int(port)
    except ValueError:
        print("Invalid port number")
        port = None
        
    if port is not None:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', port))
        server_socket.listen(1)
        print("Server listening on port " + str(port))
        
        while True:
            client_socket, address = server_socket.accept()
            print("Got connection from " + address[0])
            
            client_socket.send("Hello, world!")
            
            client_socket.close()
            server_socket.close()
    else:
        print("No port number given")
        
