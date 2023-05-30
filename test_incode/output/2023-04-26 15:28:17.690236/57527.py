#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and removes user input. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant', 'bird', 'snake', 'bird', 'cat', 'dog', 'mouse', 'elephant', 'bird', 'snake', 'bird']
    
    words_to_remove = []
    
    for word in words:
        if word == 'cat':
            words_to_remove.append('cat')
        elif word == 'dog':
            words_to_remove.append('dog')
        elif word == 'mouse':
            words_to_remove.append('mouse')
        elif word == 'elephant':
            words_to_remove.append('elephant')
        elif word == 'bird':
            words_to_remove.append('bird')
        elif word == 'snake':
            words_to_remove.append('snake')
        elif word == 'bird':
            words_to_remove.append('bird')
        elif word == 'cat':
            words_to_remove.append('cat')
        elif word == 'dog':
            words_to_remove.append('dog')
        elif word == 'mouse':
            words_to_remove.append('mouse')
        elif word == 'elephant':
            words_to_remove.append('elephant')
        elif word == 'bird':
            words_to_remove.append('bird')
        elif word == 'snake':
            words_to_remove.append('snake')
        elif word == 'bird':
            words_to_remove.append('bird')
    
    for word in words_to_remove:
        words.remove(word)
    
    print('\n'.join(words))
    
