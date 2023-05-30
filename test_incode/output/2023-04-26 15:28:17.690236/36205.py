#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or converts numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            print('Goodbye')
            break
        else:
            number = input('Enter a number: ')
            if number.isdigit():
                number = int(number)
            else:
                print('Not a number')
                continue
            
            if word not in wordlist:
                wordlist.append(word)
                
            if number not in numberlist:
                numberlist.append(number)
                
            print('%s is %d years old' % (word, number))
            
            print('