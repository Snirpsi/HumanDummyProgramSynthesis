#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or prints all ports. """    
    port = int(sys.argv[1])
    words = []
    
    # Create a socket and bind it to the port number
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection and print its content
    while True:
        conn, addr = sock.accept()
        print('Got connection from', addr)
        
        # Receive the request and print it
        data = conn.recv(1024)
        print('Request from', addr)
        
        # Send the response to the client
        conn.sendall(b'OK')
        
        # Close the connection
        conn.close()
        
        # Append the received data to the list
        words.append(data)
        
        # Send the list to the client
        conn.sendall(bytes(words, 'utf8'))
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received data:', data)
        
        # Close the connection
        conn.close()
        
        # 