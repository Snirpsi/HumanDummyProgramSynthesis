#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and iterates over a port. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Open the port and read all words from it
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            conn.send(b'OK')
            conn.close()
            
            # Read all words and append them to the list
            words.extend(conn.recv(1024).decode().split())
            
            # Close the connection
            conn.close()
    
    # Print the list
    print('\n'.join(words))
    
    # Close the socket
    s.close()
    
