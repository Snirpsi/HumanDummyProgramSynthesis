#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and stores words. """    
    
    words = []
    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 0:
            print('Sorry, that number is negative.')
            continue
        
        words.append(str(number))
        
        if len(words) == 10:
            break
    
    print('The numbers are:')
    
    for number in words:
        print(number)
        
    print('The sum of the numbers is ' + str(sum(words)))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(words))
    
    print('The smallest number is', min(words))
    
    print('The average of the numbers is ' + str(sum(words) / len(words)))
    
    print('The largest number is', max(word