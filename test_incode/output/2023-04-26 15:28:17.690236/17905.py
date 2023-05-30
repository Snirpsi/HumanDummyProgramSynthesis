#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or opens a list of words. """    
    
    words = []
    
    # Iterate over words and print them to the screen
    for word in words:
        print(word)
        
    # Open a list of words and print them to the screen
    with open("words.txt", "r") as f:
        words = f.readlines()
    
    # Print the words to the screen
    for word in words:
        print(word)
        
    # Close the file
    f.close()
    
    # 