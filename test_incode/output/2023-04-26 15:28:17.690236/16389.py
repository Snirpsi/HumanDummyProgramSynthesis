#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and opens a list of words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    
    for index, number in enumerate(numbers):
        print(words[index])
    
    print("The numbers are:")
    for number in numbers:
        print(number)
    
    print("The words are:")
    for word in words:
        print(word)
    
    print("The length of the words are:")
    print(len(words))
    
    print("The length of the numbers are:")
    print(len(numbers))
    
    print("The sum of the numbers are:")
    print(sum(numbers))
    
    print("The sum of the words are:")
    print(sum(words))
    
    print("The difference of the numbers are:")
    print(numbers - words)
    
    print("The difference of the words are:")
    print(words - numbers)
    
    print("The product of the numbers are:")
    print(numbers * words)
    
    print("The product of the words are:")
    print(words * numbers)
    
    print("The quotient of the numbers are:")
    print(numbers / words)
    
    print("The quotient of the words are:")
    print(words / numbers)
    
    print("The remainder of the numbers are:")
    print(numbers % words)
    
    print("The remainder of the words are:")
    print(words % numbers)
    
    print("The absolute value of the numbers are:")
    print(abs(numbers))
    
    print("The absolute value of the words are:")
    print(abs(words))
    
    print("The square root of the numbers are:")
    print(math.sqrt(numbers))
    
    print("The square root of the words are:")
    print(math.sqrt(words))
    
    print("The square root of the sum of the numbers are:")
    print(math.sqrt(sum(numbers)))
    
    print("The square root of the sum of the words are:")
    print(math.sqrt(sum(words)))
    
    print("The square root of the difference of the numbers are:")
    print(math.sqrt(numbers - words))
    
    print("The square root of the difference of the words are:")
    print(math.sqrt(words - numbers))
    
    print("The square root of the product of the numbers are:")
    print(math.sqrt(numbers * words))
    
    print("The square root of the product of the words are:")
    print(math.sqrt(words * numbers))
    
    print("The square root of the quotient of the numbers are:")
    print(math.sqrt(numbers / words))
    
    print("The square root of the quotient of the words are:")
    print(math.sqrt(words / numbers))
    
    print("The square root of the remainder of the numbers are:")
    print(math.sqrt(numbers % 