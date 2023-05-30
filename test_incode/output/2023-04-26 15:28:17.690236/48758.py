#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or enumerates a list of words. """    
    
    # Open the fruit list
    fruit = open('fruits.txt', 'r')
    
    # Open the wordlist
    wordlist = open('wordlist.txt', 'r')
    
    # Read each word from the wordlist
    words = []
    for line in wordlist:
        words.append(line.strip())
    
    # Read each fruit from the fruitlist
    fruits = []
    for line in fruit:
        fruits.append(line.strip())
    
    # Print the fruit list
    print('\n'.join(fruits))
    
    # Print the wordlist
    print('\n'.join(words))
    
    # Close the fruitlist
    fruit.close()
    
    # Close the wordlist
    wordlist.close()
    
    # Close the fruit list
    fruit.close()
    
    # Close the program
    exit()
    
