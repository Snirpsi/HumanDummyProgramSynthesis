#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and removes a list of numbers. """    
    
    # Create a socket and bind to port 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 5005))
    sock.listen(1)
    
    # Accept connection and accept new connection
    client, addr = sock.accept()
    
    # Accept new connection and print its number
    while True:
        number = client.recv(1024).decode()
        print(number)
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())
        
        # Accept new connection and print its number
        client.send(number.encode())