#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words and removes a list of numbers. """    
    
    words = input("Enter a sentence: ")
    
    words = words.split()
    
    words = [word for word in words if word not in numbers]
    
    words = " ".join(words)
    
    print(words)
    
