#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or opens numbers. """    
    
    words_to_remove = input("Enter a word: ")
    
    if words_to_remove in words_to_remove.split():
        words_to_remove = words_to_remove.split()
        words_to_remove.remove('number')
        words_to_remove.remove('word')
        words_to_remove.remove('open')
        words_to_remove.remove('close')
        words_to_remove.remove('')
        
        print(" ".join(words_to_remove))
    else:
        print("No words found")
        
