#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and calculates a list of numbers. """    
    words = []
    numbers = []
    
    while True:
        words.append(input('Enter a word: '))
        numbers.append(int(input('Enter a number: ')))
        
        if words[-1] == 'stop':
            break
        
    print('The words are:')
    for word in words:
        print(word)
    print('The numbers are:')
    for number in numbers:
        print(number)
        
    print('The total is', sum(numbers))
    print('The average is', sum(numbers) / len(numbers))
    print('The median is', sorted(numbers)[len(numbers)//2])
    print('The mode is', sorted(numbers)[len(numbers)//2])
    print('The mode is', sorted(numbers)[len(numbers)//2])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
