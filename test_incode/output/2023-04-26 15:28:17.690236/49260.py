#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or calculates numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('The word is', word)
            number = input('Enter a number: ')
            if number == 'quit':
                break
            else:
                number = int(number)
                print('The number is', number)
                answer = word*number
                print('The answer is', answer)
                
