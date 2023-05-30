#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and calculates words. """    
    numbers = []
    words = []
    
    while True:
        numbers.append(int(input('Enter a number: ')))
        words.append(str(numbers))
        
        if len(words) == 5:
            break
    
    print('The words are: ')
    for word in words:
        print(word)
    
    print('The numbers are: ')
    for number in numbers:
        print(number)
    
    print('The sum of the numbers is ' + str(sum(numbers)))
    
    print('The average of the numbers is ' + str(sum(numbers) / len(numbers)))
    
    print('The median of the numbers is ' + str(