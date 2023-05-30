#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and returns a port. """    
    port = int(input("Enter a port: "))
    
    words = []
    
    for line in open("words.txt"):
        line = line.strip()
        words.append(line)
        
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for 