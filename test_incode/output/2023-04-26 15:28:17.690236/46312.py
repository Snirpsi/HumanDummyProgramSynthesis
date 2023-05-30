#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or removes words. """    
    ports = input("Enter a port number: ")
    words = input("Enter a word: ")
    words = words.split()
    
    ports = ports.strip()
    words = words.strip()
    
    ports = ports.split(",")
    words = words.split(",")
    
    ports = [int(p) for p in ports]
    words = [w.strip() for w in words]
    
    ports = [p for p in ports if p > 0]
    words = [w for w in words if w > 0]
    
    ports = list(set(ports))
    words = list(set(words))
    
    ports.sort()
    words.sort()
    
    ports = ",".join(str(p) for p in ports)
    words = ",".join(w for w in words)
    
    print("Ports: " + ports)
    print("Words: " + words)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
