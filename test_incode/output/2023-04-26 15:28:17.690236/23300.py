#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or opens user input. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        print("Opening port ", port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        print("Closed port ", port)
        
