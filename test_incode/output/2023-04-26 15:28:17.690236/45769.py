#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruit|words>" % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    if fruit == 'fruit':
        fruit = input("Enter a fruit: ")
        
    if fruit == 'words':
        words = input("Enter a list of words: ")
        
    words = words.split()
    
    fruits = fruit.split()
    
    fruits.sort()
    
    for word in words:
        if word in fruits:
            print(word)
        else:
            print("%s is not in any fruit." % word)
    
