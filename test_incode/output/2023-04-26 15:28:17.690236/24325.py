#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or calculates fruits. """    
    
    words = ["apple", "banana", "cherry"]
    fruits = ["apple", "banana", "cherry"]
    
    # Calculate fruits:
    fruits_calc = calculate_fruits(fruits)
    
    # Calculate words:
    words_calc = calculate_words(words)
    
    # Print fruits and words:
    print("Fruits:", fruits_calc)
    print("Words:", words_calc)
    
    # Print the product of fruits and words:
    print("Fruits and words:", fruits_calc 