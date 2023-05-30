#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and stores a list of words. """    
    
    words = []
    numbers = []
    
    # Read numbers from stdin
    for line in sys.stdin:
        numbers.append(int(line))
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
    
    # Add numbers and words to list
    words.extend(numbers)
    words.extend(words)
    
    # Print the list
    for word in words:
        print(word)
    
    # Print the length of the list
    print(len(words))
    
    # Print the longest word
    print(max(words))
    
    # Print the shortest word
    print(min(words))
    
    # Print the average of the numbers
    print(sum(numbers) / len(numbers))
    
    # Print the average of the words
    print(sum(words) / len(words))
    
    # Print the longest and shortest word
    print(max(words), min(words))
    
    # Print the average of the numbers and words
    print(sum(numbers) / len(numbers), sum(words) / len(words))
    
    # Print the average of the numbers and words and print them in reverse order
    print(sum(numbers) / len(numbers), sum(words) / len(words), *reversed(words))
    
    # Print the average of the numbers and words and print them in reverse order and print them in reverse order
    print(sum(numbers) / len(numbers), sum(words) / len(words), *reversed(words), *reversed(numbers))
    
    # Print the average of the numbers and words and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print them in reverse order and print 