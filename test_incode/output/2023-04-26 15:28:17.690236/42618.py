#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    # Open a socket to listen on port 5000.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 5000))
    sock.listen(1)
    
    # Accept a connection from the client.
    client, addr = sock.accept()
    
    # Receive the message from the client.
    message = client.recv(1024)
    
    # Close the client socket.
    client.close()
    
    # Send the message back to the client.
    client.send(message)
    
    # Close the server socket.
    sock.close()

<|/ file source=github ext=.py |>