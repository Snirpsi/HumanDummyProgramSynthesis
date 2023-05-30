#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or adds user input. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number.")
            continue
        else:
            break
    
    # Open a port and wait for it to open
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", port))
    sock.listen(1)
    
    # Accept connection and print its address
    client, address = sock.accept()
    print("Connected by", address)
    
    # Receive data from the client
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("Received: '%s'" % data.decode())
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
