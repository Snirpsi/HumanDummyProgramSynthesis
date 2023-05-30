#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or calculates all ports. """    
    port = int(input('Enter a port number: '))
    
    # Open the port and print its contents
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    while True:
        connection, address = sock.accept()
        print('Connected by', address)
        data = connection.recv(1024)
        connection.close()
        
        # Send the result back to the client
        connection.send(data)
    
    sock.close()
