#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and prints user input. """    
    
    words_to_remove = input("Enter the words to remove: ")
    
    words_to_remove = words_to_remove.split()
    
    for word in words_to_remove:
        word = word.strip()
        
        if word == '' or word == '.':
            continue
        
        if word not in stopwords.