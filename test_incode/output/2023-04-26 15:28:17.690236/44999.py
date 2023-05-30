#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and iterates over a list of numbers. """    
    port = int(sys.argv[1])
    ports = [int(port)]
    
    # Open a socket to listen on port 0.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(5)
    
    # Loop until a connection is made and closed.
    while True:
        # Accept a connection and make a file-like object out of it.
        conn, addr = sock.accept()
        
        # Create a file-like object from the connection.
        f = io.TextIOWrapper(conn, encoding='utf8')
        
        # Read and decode the file line by line.
        for line in f:
            # Remove the first line of the file because it is empty.
            line = line[1:]
            
            # Remove all spaces from the line.
            line = line.strip()
            
            # Remove all non-digit characters from the line.
            line = line.translate(None, '0123456789')
            
            # If the line is a valid number, add it to the list of ports.
            if line:
                ports.append(int(line))
        
        # Close the connection and exit the loop.
        f.close()
        conn.close()
        
        # Print the list of ports.
        print('\n'.join(map(str, ports)))
        
        # Close the socket.
        sock.close()
        
        # Wait for a second before 