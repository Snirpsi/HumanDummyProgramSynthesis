#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and multiplyes a list of words. """    
    numbers = range(10)
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    # Iterate over the numbers and words and multiply them together
    for number, word in zip(numbers, words):
        print("{} * {} = {}".format(number, word, number * word))
        
    # Print the final result
    print("The final result is {}".format(numbers * words))
    
    # 