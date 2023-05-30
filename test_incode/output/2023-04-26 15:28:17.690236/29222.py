#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and multiplyes numbers. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
        
        numbers = []
        
        for number in range(1, int(input("Enter a number: "))+1):
            numbers.append(number)
            
        numbers = list(map(lambda x: x*x, numbers))
        
        numbers = list(map(lambda x: str(x), numbers))
        
        print("The word '{}' multiplied by {} is: {}".format(word, numbers[0], numbers[1]))
        
        words.append(numbers[0])
        
        numbers = []
        
        for number in range(2, int(input("Enter a number: "))+1):
            numbers.append(number)
            
        numbers = list(map(lambda x: x*x, numbers))
        
        numbers = list(map(lambda x: str(x), numbers))
        
        print("The word '{}' multiplied by {} is: {}".format(word, numbers[0], numbers[1]))
        
        words.append(numbers[0])
        
        numbers = []
        
        for number in range(3, int(input("Enter a number: "))+1):
            numbers.append(number)
            
        numbers = list(map(lambda x: x*x, numbers))
        
        numbers = list(map(lambda x: str(x), numbers))
        
        print("The word '{}' multiplied by {} is: {}".format(word, numbers[0], numbers[1]))
        
        words.append(numbers[0])
        
        numbers = []
        
        for number in range(4, int(input("Enter a number: "))+1):
            numbers.append(number)
            
        numbers = list(map(lambda x: x*x, numbers))
        
        numbers = list(map(lambda x: str(x), numbers))
        
        print("The word '{}' multiplied by {} is: {}".format(word, numbers[0], numbers[1]))
        
        words.append(numbers[0])
        
        numbers = []
        
        for number in range(5, int(input("Enter a number: "))+1):
            numbers.append(number)
            
        numbers = list(map(lambda x: x*x, numbers))
        
        numbers = list(map(lambda x: str(x), numbers))
        
        print("The word '{}' multiplied by {} is: {}".format(word, numbers[0], numbers[1]))
        
        words.append(numbers[0])
        
        numbers = []
        
        for number in range(6, int(input("Enter a number: "))+1):
            numbers.append(number)
            
        numbers = list(map(lambda x: x*x, numbers))
        
        numbers = list(map(lambda x: str(x), numbers))
        
        print("The word '{}' multiplied by {} is: {}".format(word, numbers[0], numbers[1]))
        
        words.append(numbers[0])
        
        numbers = []
        
        for number in range(7, int(input("Enter 