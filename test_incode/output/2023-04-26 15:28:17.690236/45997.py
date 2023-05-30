#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words or removes a list of words. """    
    
    words_list = input("Enter the list of words: ")
    
    if words_list:
        words = words_list.split()
        
        remove_list = input("Enter the list of words to remove: ")
        
        if remove_list:
            remove_list = remove_list.split()
            
            remove_list.remove('all')
            
            words = words + remove_list
            
            print("\n".join(words))
        else:
            print("\n".join(words))
    else:
        print("No words given.")
    
