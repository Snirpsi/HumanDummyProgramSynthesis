#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or adds a list of words. """    
    while True:
        try:
            line = input('Enter a number: ')
            number = int(line)
        except ValueError:
            print('Invalid input')
            continue
        else:
            break
    
    numbers = []
    while True:
        try:
            line = input('Enter a word: ')
            word = str(line)
        except ValueError:
            print('Invalid input')
            continue
        else:
            numbers.append(word)
            break
    
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    print('The words are:')
    for word in numbers:
        print(word)
    
    print('The total is:', sum(numbers))
    
    print('The average is:', sum(numbers) / len(numbers))
    
    print('The standard deviation is:', 
          math.sqrt((sum([pow(number, 2) for number in numbers]) -
                    sum([pow(number, 2) for number in numbers])) ** 2) / len(numbers))
    
    print('The mode is:', 
          max(numbers), 
          min(numbers), 
          max(numbers), 
          min(numbers), 
          sum(numbers), 
          len(numbers))
    
    print('The median is:', 
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)])
    
    print('The mode is:', 
          max(numbers), 
          min(numbers), 
          max(numbers), 
          min(numbers), 
          sum(numbers), 
          len(numbers))
    
    print('The median is:', 
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)])
    
    print('The mode is:', 
          max(numbers), 
          min(numbers), 
          max(numbers), 
          min(numbers), 
          sum(numbers), 
          len(numbers))
    
    print('The median is:', 
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)],
          sorted(numbers)[int(len(numbers) / 2)])
    
    print('