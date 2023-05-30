#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    words = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million',
        'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion',
        'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion',
        'tredecillion', 'quattuordecillion', 'quinquadecillion', 'sexdecillion',
        'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion'
    ]
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(words[int(word)])
    
