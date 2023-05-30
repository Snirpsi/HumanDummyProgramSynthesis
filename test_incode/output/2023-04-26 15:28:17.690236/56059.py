#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    while True:
        word = input("Enter a word: ")
        word_length = len(word)
        
        if word_length < 3:
            print("Too short, try again.")
            continue
        
        word_list = list(word)
        
        if word_list[0] == 'a':
            word_list[1] = 'e'
            word_list[2] = 'i'
        elif word_list[0] == 'e':
            word_list[1] = 'i'
            word_list[2] = 'o'
        elif word_list[0] == 'i':
            word_list[1] = 'o'
            word_list[2] = 'u'
        elif word_list[0] == 'o':
            word_list[1] = 'u'
            word_list[2] = 'i'
        elif word_list[0] == 'u':
            word_list[1] = 'i'
            word_list[2] = 'a'
        elif word_list[0] == 'i':
            word_list[1] = 'a'
            word_list[2] = 'e'
        elif word_list[0] == 'e':
            word_list[1] = 'e'
            word_list[2] = 'i'
        elif word_list[0] == 'i':
            word_list[1] = 'i'
            word_list[2] = 'o'
        elif word_list[0] == 'o':
            word_list[1] = 'o'
            word_list[2] = 'u'
        elif word_list[0] == 'u':
            word_list[1] = 'u'
            word_list[2] = 'a'
        else:
            print("Invalid input.")
            continue
        
        word_list = list("".join(word_list))
        
        word_list = list("".join(word_list))
        
        if word_list[0] == 'a':
            word_list[1] = 'e'
            word_list[2] = 'i'
        elif word_list[0] == 'e':
            word_list[1] = 'i'
            word_list[2] = 'o'
        elif word_list[0] == 'i':
            word_list[1] = 'o'
            word_list[2] = 'u'
        elif word_list[0] == 'o':
            word_list[1] = 'u'
            word_list[2] = 'i'
        elif word_list[0] == 'u':
            word_list[1] = 'i'
            word_list[2] = 'a'
        elif word_list[0] == 'i':
            word_list[1] = 'a'
            word_list[2] = 'e'
        elif word_list[0] == 'e':
            word_list[1] = 'e'
            word_list[2] = 'i'
        elif word_list[0] == 'i':
            word_list[1] = 'i'
            word_list[2] = 'o'
        elif word_list[0] == 'o':
            word_list[1] = 'o'
            word_list[2] = 'u'
        elif word_list[0] == 'u':
            word_list[1] = 'u'
            word_list[2] = 'a'
        else:
            print("