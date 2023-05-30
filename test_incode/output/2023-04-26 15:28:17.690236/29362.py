#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and converts all ports. """    
    ports = input("Enter ports: ")
    ports = ports.split()
    ports = [int(p) for p in ports]
    ports = list(set(ports))
    ports.sort()
    ports = ports[:10]
    
    ports_str = " ".join(str(p) for p in ports)
    
    ports_str = ports_str.replace("[","")
    ports_str = ports_str.replace("]","")
    ports_str = ports_str.replace("'","")
    ports_str = ports_str.replace("(","")
    ports_str = ports_str.replace(")","")
    ports_str = ports_str.replace(",","")
    ports_str = ports_str.replace(":","")
    ports_str = ports_str.replace("-","")
    ports_str = ports_str.replace("+","")
    ports_str = ports_str.replace("*","")
    ports_str = ports_str.replace("/","")
    
    ports_str = ports_str.replace("'","")
    
    ports_str = ports_str.replace("[","")
    ports_str = ports_str.replace("]","")
    ports_str = ports_str.replace("'","")
    
    ports_str = ports_str.replace("(","")
    ports_str = ports_str.replace(")","")
    
    ports_str = ports_str.replace(",","")
    ports_str = ports_str.replace(":","")
    ports_str = ports_str.replace("-","")
    ports_str = ports_str.replace("+","")
    ports_str = ports_str.replace("*","")
    ports_str = ports_str.replace("/","")
    
    ports_str = ports_str.replace("'","")
    
    ports_str = ports_str.replace("[","")
    ports_str = ports_str.replace("]","")
    ports_str = ports_str.replace("'","")
    
    ports_str = ports_str.replace("(","")
    ports_str = ports_str.replace(")","")
    
    ports_str = ports_str.replace(",","")
    ports_str = ports_str.replace(":","")
    ports_str = ports_str.replace("-","")
    ports_str = ports_str.replace("+","")
    ports_str = ports_str.replace("*","")
    ports_str = ports_str.replace("/","")
    
    ports_str = ports_str.replace("'","")
    
    ports_str = ports_str.replace("[","")
    ports_str = ports_str.replace("]","")