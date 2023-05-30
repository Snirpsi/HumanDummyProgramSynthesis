#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or converts words. """    
    
    words = []
    
    while True:
        try:
            words.append(int(input("Enter a number: ")))
        except ValueError:
            words.append(input("Enter a number: "))
        
        if words[-1] == "":
            words.pop()
            
        if len(words) == 0:
            break
    
    print("\n".join(map(str, words)))
    
