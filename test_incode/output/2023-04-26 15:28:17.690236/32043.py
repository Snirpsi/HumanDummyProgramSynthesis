#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or enumerates words. """    
    
    # Read user input
    word = input("Enter a word: ")
    
    # Enumerate words
    words = word.split()
    for word in words:
        print(word)
        
    # Write to file
    with open('words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')
            
    # Close file
    f.close()
    
    # 