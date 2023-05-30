#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and removes user input. """    
    
    port = int(input("Enter a port number: "))
    
    while(True):
        print("\nListening on port " + str(port))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", port))
        sock.listen(1)
        
        client, address = sock.accept()
        
        message = client.recv(1024)
        
        client.close()
        
        print("Received: %s" % message)
        
        sock.close()
        
        print("Closing port")
        
        port -= 1
        
