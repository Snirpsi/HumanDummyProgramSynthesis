#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and removes user input. """    
    
    port = int(input("Enter the port to listen to: "))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        conn.close()
        
        print("Server has disconnected.")
    
    sock.close()
    
