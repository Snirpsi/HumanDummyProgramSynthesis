#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and iterates over all ports. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        print("Port", port, "is open.")
        
        while True:
            line = input("Enter next line: ")
            if line == "exit":
                break
            
            print(line)
            
