#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and stores words. """    
    
    while True:
        port = input("Enter a port number: ")
        words = []
        
        # Open a socket and connect to the port.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((port, 80))
        
        # Read all data sent from the socket and store it in a list.
        while True:
            data = sock.recv(1024)
            if not data:
                break
            words.append(data.decode())
        
        # Close the socket and print all received data.
        sock.close()
        
        # Print all received data.
        print("Received: ", end="")
        for word in words:
            print(word, end="")
        print()
        
        # Wait for a key press.
        