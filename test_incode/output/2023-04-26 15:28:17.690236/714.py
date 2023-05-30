#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and converts words. """    
    while True:
        port = int(input("Enter a port number: "))
        words = []
        
        # Open a port and listen for words.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        # Wait for connections.
        conn, addr = sock.accept()
        
        # Receive a message from the client.
        message = conn.recv(1024)
        
        # Convert each word to lowercase.
        words = message.lower().split()
        
        # Send the converted words to the client.
        for word in words:
            conn.send(word.encode('utf-8'))
            
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
            print(word)
        
        # Wait for a new message.
        message = conn.recv(1024)
        
        # Close the connection.
        conn.close()
        
        # Print the received words.
        for word in words:
