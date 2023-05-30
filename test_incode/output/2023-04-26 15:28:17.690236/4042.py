#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or prints user input. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('You entered', len(words), 'words')
    print('The first word is', words[0])
    print('The last word is', words[-1])
    print('The middle word is', words[int(len(words) / 2)])
    print('The middle word is', words[int(len(words) / 2)-1]