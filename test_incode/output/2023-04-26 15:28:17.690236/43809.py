#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or enumerates words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        elif number > 0:
            for word in words:
                if number % 2 == 0:
                    print(word)
                else:
                    print(words[number // 2])
        else:
            print('That number is too large')
        
