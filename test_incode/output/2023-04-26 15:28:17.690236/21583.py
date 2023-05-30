#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers and multiplyes words. """    
    while True:
        words = []
        numbers = []
        
        while True:
            number = input('Enter a number: ')
            if number.isdigit():
                numbers.append(int(number))
            else:
                words.append(number)
                break
        
        while True:
            word = input('Enter a word: ')
            if word.isdigit():
                words.append(int(word))
            else:
                words.append(word)
                break
        
        numbers = list(map(int, numbers))
        words = list(map(str, words))
        
        numbers = numbers * len(words)
        words = words * len(numbers)
        
        print(' '.join(words))
        print(' '.join(numbers))
        
        print('Press enter to exit')
        input()
