#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and prints a list of words. """    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    words = [str(numbers[i]*numbers[i+1]) for i in range(len(numbers)-1)]
    print(" ".join(words))
    
