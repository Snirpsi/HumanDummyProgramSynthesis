#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input('Enter a port number: ')
        
        # Open the port and read its contents
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send('GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n')
        
        # Read the response and print it
        response_data = sock.recv(1024)
        print('Response from server:')
        print(response_data)
        
        # Close the connection
        sock.close()
        
        # Wait for next request
        time.sleep(1)
        
        # Close the port
        sock.close()
        
        # Close the socket
        sock.close()
        
        # Close the server
        