#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or adds a list of numbers. """    
    while True:
        numbers = input("Enter numbers: ").split()
        numbers = [int(x) for x in numbers]
        
        answer = sum(numbers)
        print("The answer is", answer)
        
        if numbers[0] == "exit":
            break
        
        if numbers[0] == "add":
            numbers = numbers[1:]
            answer = sum(numbers)
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "subtract":
            numbers = numbers[1:]
            answer = numbers[0] - numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "divide":
            numbers = numbers[1:]
            answer = numbers[0] / numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "divide":
            numbers = numbers[1:]
            answer = numbers[0] / numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "divide":
            numbers = numbers[1:]
            answer = numbers[0] / numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "divide":
            numbers = numbers[1:]
            answer = numbers[0] / numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "divide":
            numbers = numbers[1:]
            answer = numbers[0] / numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "divide":
            numbers = numbers[1:]
            answer = numbers[0] / numbers[1]
            print("The answer is", answer)
        
        if numbers[0] == "multiply":
            numbers = numbers[1:]
            answer = numbers[0] * numbers[1]
            print("The answer is", answer)
        