#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and iterates over words. """    
    
    numbers = []
    words = []
    
    while True:
        number = input('Enter a number: ')
        numbers.append(number)
        
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
    print('Numbers: ', numbers)
    print('Words: ', words)
    
    print('The sum of the numbers is ', sum(numbers))
    print('The sum of the words is ', sum(words))
    
    print('The average of the numbers is ', sum(numbers) / len(numbers))
    print('The average of the words is ', sum(words) / len(words))
    
    print('The largest number in the numbers is ', max(numbers))
    print('The largest number in the words is ', max(words))
    
    print('The smallest number in the numbers is ', min(numbers))
    print('The smallest number in the words is ', min(words))
    
    print('The median of the numbers is ', sorted(numbers)[len(numbers)//2])
    print('The median of the words is ', sorted(words)[len(words)//2])
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(numbers), min(numbers), sum(numbers), len(numbers))
    print('The mode of the words is ', max(words), min(words), sum(words), len(words))
    
    print('The mode of the numbers is ', max(