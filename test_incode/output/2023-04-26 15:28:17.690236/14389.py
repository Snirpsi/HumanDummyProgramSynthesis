#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or calculates all ports. """    
    
    ports = []
    while True:
        ports.append(input("Enter a port number: "))
        
        if ports[-1].isdigit():
            ports.pop()
        else:
            break
    
    ports = list(map(int, ports))
    
    ports.sort()
    
    ports_str = str(ports)
    
    ports_str = ports_str[1:-1]
    
    ports_str = ports_str.replace("[", "").replace("]", "")
    
    ports_str = ports_str.replace("'", "")
    
    ports_str = ports_str.replace(",", "")
    
    ports_str = ports_str.replace("(", "")
    
    ports_str = ports_str.replace(")", "")
    
    ports_str = ports_str.replace(",", "")
    
    ports_str = ports_str.replace("-", "")
    
    ports_str = ports_str.replace("+", "")
    
    ports_str = ports_str.replace("*", "")
    
    ports_str = ports_str.replace("%", "")
    
    ports_str = ports_str.replace("=", "")
    
    ports_str = ports_str.replace("(", "")
    
    ports_str = ports_str.replace(")", "")
    
    ports_str = ports_str.replace(",", "")
    
    ports_str = ports_str.replace("-", "")
    
    ports_str = ports_str.replace("+", "")
    
    ports_str = ports_str.replace("*", "")
    
    ports_str = ports_str.replace("%", "")
    
    ports_str = ports_str.replace("=", "")
    
    ports_str = ports_str.replace("(", "")
    
    ports_str = ports_str.replace(")", "")
    
    ports_str = ports_str.replace(",", "")
    
    ports_str = ports_str.replace("-", "")
    
    ports_str = ports_str.replace("+", "")
    
    ports_str = ports_str.replace("*", "")
    
    ports_str = ports_str.replace("%", "")
    
    ports_str = ports_str.replace("=", "")
    
    ports_str = ports_str.replace("(", "")
    
    ports_str = ports_str.replace(")", "")
    
    ports_str = ports_str.replace(",", "")
    
    ports_str = ports_str.replace("-", "")
    
    ports_str = ports_str.replace("+", "")
    
    ports_str = ports_str.replace("*