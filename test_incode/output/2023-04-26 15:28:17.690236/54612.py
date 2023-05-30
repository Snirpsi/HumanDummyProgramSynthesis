#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and calculates a list of numbers. """    
    words = []
    numbers = []
    
    # Read a file and split it into words
    with open('words.txt') as file:
        words = file.read().split()
    
    # Read a file and split it into numbers
    with open('numbers.txt') as file:
        numbers = file.read().split()
    
    # Print the words and numbers
    print('Words:', words)
    print('Numbers:', numbers)
    
    # Calculate the sum of numbers and words
    numbers_sum = sum(numbers)
    words_sum = sum(words)
    
    # Print the sum of the numbers and the sum of the words
    print('The sum of the numbers is ' + str(numbers_sum))
    print('The sum of the words is ' + str(words_sum))
    
    # Print the average of the numbers and the sum of the words
    print('The average of the numbers is ' + str(numbers_sum/len(numbers)))
    print('The average of the words is ' + str(words_sum/len(words)))
    
    # Print the sum of the numbers and the average of the words
    print('The sum of the numbers and the average of the words is ' + str(numbers_sum/len(numbers)) + ', and the sum of the words and the average of the words is ' + str(words_sum/len(words)) + ', respectively.')
    
    # Print the sum of all numbers and the sum of all words
    print('The sum of all numbers is ' + str(sum(numbers)))
    print('The sum of all words is ' + str(sum(words)))
    
    # Print the difference of the sum of all numbers and the sum of all words
    print('The difference of the sum of all numbers and the sum of all words is ' + str(numbers_sum - words_sum))
    
    # Print the difference of the average of the numbers and the sum of all words
    print('The difference of the average of the numbers and the sum of all words is ' + str(numbers_sum/len(numbers)) - ', and the difference of the sum of all words and the average of the words is ' + str(words_sum/len(words)) - ', respectively.')
    
    # Print the difference of the sum of all numbers and the average of the words
    print('The difference of the sum of all numbers and the average of the words is ' + str(numbers_sum/len(numbers)) + ', and the difference of the average of the words and the sum of all words is ' + str(words_sum/len(words)) + ', respectively.')
    
    # Print the difference of the sum of all numbers and the average of the words
    print('The difference of the sum of all numbers and the average of the words is ' + str(numbers_sum/len(numbers)) + ', and the difference of the average of the words and the sum of all words is ' + str(words_sum/len(words)) + ', respectively.')
    
    # Print the difference of the sum of all numbers and the average of the words
    print('The difference of the sum of all numbers and the average of the words is ' + str(numbers_