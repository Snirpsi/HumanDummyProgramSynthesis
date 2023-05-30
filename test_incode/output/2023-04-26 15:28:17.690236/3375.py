#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and multiplyes user input. """    
    words = ['one', 'two', 'three']
    
    for word in words:
        word = word.lower()
        word = word.capitalize()
        word = word.replace(' ', '')
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.replace('-', '')
        word = word.replace(':', '')
        word = word.replace(';', '')
        word = word.replace('?', '