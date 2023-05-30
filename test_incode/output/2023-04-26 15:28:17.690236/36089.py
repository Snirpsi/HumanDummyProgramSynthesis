#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or iterates over user input. """    
    port = int(input("Enter a port to convert or enter 0 to exit: "))
    
    if port == 0:
        print("Exiting...")
        sys.exit()
    
    ports = [port]
    
    while True:
        port = input("Enter a port to convert or enter 0 to exit: ")
        
        if port == 0:
            print("Exiting...")
            sys.exit()
        
        if port not in ports:
            ports.append(port)
            
        else:
            print("Port already converted. Try again.")
    
