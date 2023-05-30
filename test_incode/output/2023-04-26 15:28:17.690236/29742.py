#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and multiplyes numbers. """    
    words = input("Enter a sentence: ").split()
    numbers = [int(i) for i in words]
    product = numbers[0]
    for number in numbers[1:]:
        product = product * number
    print(product)
