#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and stores all ports. """    
    port = int(sys.argv[1])
    words = []
    
    # Open a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(5)
    
    # Accept connections and store them in the list
    while True:
        conn, addr = sock.accept()
        print('Got connection from', addr)
        
        # Receive the message from the client
        message = conn.recv(1024)
        
        # Send the message back to the client
        conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n' + message + '\r\n')
        
        # Close the connection
        conn.close()
        
        # Add the received message to the list
        words.append(message)
    
    # Close the socket
    sock.close()
    
    # Print the list
    print('\n'.join(words))
    
    # 