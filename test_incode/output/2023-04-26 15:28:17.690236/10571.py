#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or converts all ports. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        else:
            port = int(port)
            
        if port == -1:
            print("Invalid port number")
            continue
        else:
            port = int(port)
            
            if port == -1:
                print("Invalid port number")
                continue
            else:
                print("Multiplying port", port, "by", 