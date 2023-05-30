#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or stores a list of words. """    
    
    ports = [
        port for port in range(10000, 20000, 100)
        if port not in [10000, 20000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
    ]
    
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        
        if len(words) == 