#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or adds a list of words. """    
    while True:
        port = input("Enter a port number: ")
        
        if port == "exit":
            break
        
        if port == "help":
            print("Usage: python ports.py [help]")
        
        elif port == "list":
            print("Ports:")
            for port in ports:
                print("\t" + str(port))
        
        else:
            ports.append(port)
        
    print("Done")

<|/ file filename=ports.py ext=.py |>