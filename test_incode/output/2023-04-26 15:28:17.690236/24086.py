#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Open a socket and listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8080))
    sock.listen(10)
    
    # Accept a connection and make a file-like object out of it.
    while True:
        conn, addr = sock.accept()
        
        # Make a file-like object out of the connection.
        f = conn.makefile('r', encoding = 'utf-8')
        
        # Read all data until EOF.
        while True:
            data = f.read(1024)
            if not data:
                break
            
            # Append the data to the list of words.
            words.append(data)
        
        # Close the connection.
        f.close()
        
    # Print the list of words to the console.
    print('\n'.join(words))
    
    # Close the socket.
    sock.close()
    
