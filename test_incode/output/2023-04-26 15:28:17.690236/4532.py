#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and removes a list of words. """    
    numbers = []
    words = []
    
    while True:
        number = input("Enter a number: ")
        if number in numbers:
            print("That number already exists. Try again.")
            continue
        numbers.append(number)
        word = input("Enter a word: ")
        if word in words:
            print("That word already exists. Try again.")
            continue
        words.append(word)
        
        print("Number: ", number)
        print("Word: ", word)
        
        print("Would you like to add another number? Y/N: ")
        answer = input("(Y/N): ")
        if answer.lower() == "y":
            print("Adding another number...")
            number = input("Enter a number: ")
            numbers.append(number)
        elif answer.lower() == "n":
            print("Thank you for using my program!")
            break
        else:
            print("Invalid input. Please try again.")
            continue
    
    print("Numbers: ", numbers)
    print("Words: ", words)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
