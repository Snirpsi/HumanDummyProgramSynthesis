#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or calculates a list of words. """    
    
    # Open a port and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    sock.listen(1)
    
    while True:
        # Accept a connection and make a file-like object out of it
        conn, addr = sock.accept()
        
        # Open a file-like object from that connection
        f = open(conn, 'rb')
        
        # Read all data sent by the client
        data = f.read()
        
        # Close the connection
        f.close()
        
        # Send the data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # Send the received data to the client
        conn.send(data)
        
        # Close the connection
        conn.close()
        
        # Print the received data
        print('Received: {0}'.format(data))
        
        # 