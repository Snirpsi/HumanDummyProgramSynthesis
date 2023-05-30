#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and enumerates a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            words.append(word)
    
    print('The words are:')
    for word in words:
        print(word)
    
    print('\nThe word with the highest frequency is:', max(words))
    
    print('\nThe word with the lowest frequency is:', min(words))
    
    print('\nThe word with the average frequency is:', sum(words) / len(words))
    
    print('\nThe word with the largest number of vowels is:', max(set('aeiouAEIOU').difference(words)))
    
    print('\nThe word with the smallest number of vowels is:', min(set('aeiouAEIOU').difference(words)))
    
    print('\nThe word with the largest number of consonants is:', max(set('bcdfghjklmnpqrstvwxyz').difference(words)))
    
    print('\nThe word with the smallest number of consonants is:', min(set('bcdfghjklmnpqrstvwxyz').difference(words)))
    
    print('\nThe word with the largest number of digits is:', max(set('123456789').difference(words)))
    
    print('\nThe word with the smallest number of digits is:', min(set('123456789').difference(words)))
    
    print('\nThe word with the largest number of uppercase letters is:', max(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ').difference(words)))
    
    print('\nThe word with the smallest number of uppercase letters is:', min(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ').difference(words)))
    
    print('\nThe word with the largest number of lowercase letters is:', max(set('abcdefghijklmnopqrstuvwxyz').difference(words)))
    
    print('\nThe word with the smallest number of lowercase letters is:', min(set('abcdefghijklmnopqrstuvwxyz').difference(words)))
    
    print('\nThe word with the largest number of special characters is:', max(set('!@#$%^&*()_+{}[]\\|;:\'",./<>?')).difference(words))
    
    print('\nThe word with the smallest number of special characters is:', min(set('!@#$%^&*()_+{}[]\\|;:\'",./<>?')).difference(words))
    
    print('\nThe word with the largest number of special characters is:', max(set('!@#$%^&*()_+{}[]\\|;:\'",./<>?')).difference(words))
    
