#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words and enumerates a list of numbers. """    
    
    words = []
    numbers = []
    
    # Read in words and numbers from file 
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        
    with open('numbers.txt', 'r') as file:
        numbers = file.read().splitlines()
    
    # Iterate through words and numbers and add them to the lists 
    for word in words:
        for number in numbers:
            words.append(word)
            numbers.append(number)
    
    # Print the words and numbers 
    print('Words:', words)
    print('Numbers:', numbers)
    
    # Print the length of the lists 
    print('Length of words: ', len(words))
    print('Length of numbers: ', len(numbers))
    
    # Print the longest word in the words list 
    print('Longest word:', max(words))
    
    # Print the longest number in the numbers list 
    print('Longest number:', max(numbers))
    
    # Print the shortest word in the words list 
    print('Shortest word:', min(words))
    
    # Print the shortest number in the numbers list 
    print('Shortest number:', min(numbers))
    
    # Print the average length of the words list 
    print('Average length of words: ', sum(words) / len(words))
    
    # Print the average length of the numbers list 
    print('Average length of numbers: ', sum(numbers) / len(numbers))
    
    # Print the average length of the words list 
    print('Average length of words: ', sum(words) / len(words))
    
    # Print the average length of the numbers list 
    print('Average length of numbers: ', sum(numbers) / len(numbers))
    
    # Print the average length of the words list 
    print('Average length of words: ', sum(words) / len(words))
    
    # Print the average length of the numbers list 
    print('Average length of numbers: ', sum(numbers) / len(numbers))
    
    # Print the average length of the words list 
    print('Average length of words: ', sum(words) / len(words))
    
    # Print the average length of the numbers list 
    print('Average length of numbers: ', sum(numbers) / len(numbers))
    
    # Print the average length of the words list 
    print('Average length of words: ', sum(words) / len(words))
    
    # Print the average length of the numbers list 
    print('Average length of numbers: ', sum(numbers) / len(numbers))
    
    # Print the average length of the words list 
    print('Average length of words: ', sum(words) / len(words))
    
    # Print the average length of the numbers list 
    print('Average length of numbers: ', sum(numbers) / len(numbers))
    
    # Print the average length of the words list 
    print('