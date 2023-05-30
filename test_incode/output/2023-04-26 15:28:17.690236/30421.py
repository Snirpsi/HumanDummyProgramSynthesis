#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and stores a list of words. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        words.append(word)
        
    print("\nWords entered:")
    for word in words:
        print(word)
    
    print("\nWords found:")
    for word in words:
        if word in words:
            print(word)
        else:
            print("