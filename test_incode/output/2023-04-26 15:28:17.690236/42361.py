#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
            
    print('You entered', len(words), 'words')
    print('The first word was', words[0])
    print('The last word was', words[-1])
    print('The middle word was', words[int(len(words)/2)])
    print('The middle and last words were', words[int(len(words)/2)-1], words[int(len(words)/2)])
    print('The middle and first words were', words[int(len(words)/2)-2], words[int(len(words)/2)])
    print('The first and last words were', words[0], words[-1])
    print('The first and middle words were', words[0], words[int(len(words)/2)])
    print('The last and middle words were', words[-1], words[int(len(words)/2)])
    print('The last and first words were', words[-1], words[0])
    print('The first and last words were', words[0], words[-1])
    print('The middle and last words were', words[int(len(words)/2)-1], words[int(len(words)/2)])
    print('The middle and first words were', words[int(len(words)/2)-2], words[int(len(words)/2)])
    print('The first and last words were', words[0], words[int(len(words)/2)])
    print('The first and middle words were', words[0], words[int(len(words)/2)])
    print('The last and middle words were', words[-1], words[int(len(words)/2)])
    print('The last and first words were', words[-1], words[0])
    print('The first and last words were', words[0], words[-1])
    print('The middle and last words were', words[int(len(words)/2)-1], words[int(len(words)/2)])
    print('The middle and first words were', words[int(len(words)/2)-2], words[int(len(words)/2)])
    print('The first and last words were', words[0], words[int(len(words)/2)])
    print('The first and middle words were', words[0], words[int(len(words)/2)])
    print('The last and middle words were', words[-1], words[int(len(words)/2)])
    print('The last and first words were', words[-1], words[0])
    print('The first and last words were', words[0], words[-1])
    print('The middle and last words were', words[int(len(words)/2)-1], words[int(len(words)/2)])