#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and iterates over words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').lower())
        if words[-1] == 'q':
            break
    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == 'q':
            break
    
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    print('The words are:')
    for word in words:
        print(word)
    
    print('The sum of the numbers is %d' % sum(numbers))
    print('The sum of the words is %s' % sum(words))
    
    print('The average of the numbers is %.2f' % sum(numbers) / len(numbers))
    print('The average of the words is %.2f' % sum(words) / len(words))
    
    print('The largest number is', max(numbers))
    print('The largest word is', max(words))
    
    print('The smallest number is', min(numbers))
    print('The smallest word is', min(words))
    
    print('The largest number is', max(numbers))
    print('The largest word is', max(words))
    
    print('The smallest number is', min(numbers))
    print('The smallest word is', min(words))
    
    print('The average of the numbers is %.2f' % sum(numbers) / len(numbers))
    print('The average of the words is %.2f' % sum(words) / len(words))
    
    print('The largest number is', max(numbers))
    print('The largest word is', max(words))
    
    print('The smallest number is', min(numbers))
    print('The smallest word is', min(words))
    
    print('The average of the numbers is %.2f' % sum(numbers) / len(numbers))
    print('The average of the words is %.2f' % sum(words) / len(words))
    
    print('The largest number is', max(numbers))
    print('The largest word is', max(words))
    
    print('The smallest number is', min(numbers))
    print('The smallest word is', min(words))
    
    print('The average of the numbers is %.2f' % sum(numbers) / len(numbers))
    print('The average of the words is %.2f' % sum(words) / len(words))
    
    print('The largest number is', max(numbers))
    print('The largest word is', max(words))
    
    print('The smallest number is', min(numbers))
    print('The smallest word is', min(words))
    
    print('The average of the numbers is %.2f' % sum(numbers) / len(numbers))
    print('The average of the words is %.2f' % sum(words) / len(words))
    
    print('The largest number is', max(numbers))
    print('The largest word is', max(words))