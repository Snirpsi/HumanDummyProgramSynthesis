#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words and multiplyes numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Add words and multiply numbers
    words_sum = 0
    words_mult = 0
    for word in words:
        words_sum += word
        words_mult *= numbers[words.index(word)]
    
    # Print the result
    print('The sum of the words is ' + str(words_sum))
    print('The product of the numbers is ' + str(words_mult))
