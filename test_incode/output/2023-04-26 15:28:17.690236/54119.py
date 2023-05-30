#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and calculates user input. """    
    
    words = word_generator()
    
    # Calculates user input for words and prints them out
    user_answer = get_user_answer(words)
    
    print(user_answer)
    
