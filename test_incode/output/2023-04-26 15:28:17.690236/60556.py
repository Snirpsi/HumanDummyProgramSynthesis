#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and calculates fruits. """    
    
    words = []
    fruits = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Read fruits from file
    with open('fruits.txt', 'r') as f:
        for line in f:
            fruits.append(line.strip())
    
    # Calculate fruits by counting how many times each word appears
    fruits_by_count = collections.Counter(fruits)
    
    # Print the fruits sorted by number of appearance
    for fruit, count in fruits_by_count.most_common():
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
    
    # Print the fruits sorted by number of appearance in descending order
    for fruit, count in fruits_by_count.most_common(10):
        print(fruit, count)
