#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or converts words. """    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) <= 3]
    
    words = [word for word in words if len(word) <= 5]
    
    words = [word for word in words if len(word) <= 7]
    
    words = [word for word in words if len(word) <= 9]
    
    words = [word for word in words if len(word) <= 11]
    
    words = [word for word in words if len(word) <= 13]
    
    words = [word for word in words if len(word) <= 15]
    
    words = [word for word in words if len(word) <= 17]
    
    words = [word for word in words if len(word) <= 19]
    
    words = [word for word in words if len(word) <= 21]
    
    words = [word for word in words if len(word) <= 23]
    
    words = [word for word in words if len(word) <= 25]
    
    words = [word for word in words if len(word) <= 27]
    
    words = [word for word in words if len(word) <= 29]
    
    words = [word for word in words if len(word) <= 31]
    
    words = [word for word in words if len(word) <= 33]
    
    words = [word for word in words if len(word) <= 35]
    
    words = [word for word in words if len(word) <= 37]
    
    words = [word for word in words if len(word) <= 39]
    
    words = [word for word in words if len(word) <= 41]
    
    words = [word for word in words if len(word) <= 43]
    
    words = [word for word in words if len(word) <= 45]
    
    words = [word for word in words if len(word) <= 47]
    
    words = [word for word in words if len(word) <= 49]
    
    words = [word for word in words if len(word) <= 51]
    
    words = [word for word in words if len(word) <= 53]
    
    