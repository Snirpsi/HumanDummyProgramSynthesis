#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or multiplyes a list of words. """    
    
    port = int(input("Enter a port number: "))
    words = []
    
    while port > 0:
        words.append(input("Enter a word: "))
        port -= 1
    
    print("The words are:")
    for word in words:
        print(word)
        
    print("The total is ", sum(words))
    
