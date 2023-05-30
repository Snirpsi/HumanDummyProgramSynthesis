#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or adds words. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
        else:
            print("Invalid input.")
            continue
        
        if number > len(numbers):
            print("Sorry, numbers cannot be greater than the length of the list.")
            continue
        
        if number < len(numbers):
            numbers.append(number)
        else:
            print("Sorry, numbers cannot be less than the length of the list.")
            continue
        
        print("The list now contains:")
        for number in numbers:
            print(number)
        
        print("\nWould you like to add another number? [Y/N]")
        answer = input("(Y/N): ")
        if answer.lower() == "y":
            print("Enter a number: ")
            number = input("(Y/N): ")
            if number.isdigit():
                number = int(number)
            else:
                print("Invalid input.")
                continue
            
            if number > len(numbers):
                print("Sorry, numbers cannot be greater than the length of the list.")
                continue
            
            if number < len(numbers):
                numbers.append(number)
            else:
                print("Sorry, numbers cannot be less than the length of the list.")
                continue
            
            print("The list now contains:")
            for number in numbers:
                print(number)
            
            print("\nWould you like to add another number? [Y/N]")
            answer = input("(Y/N): ")
            if answer.lower() == "y":
                print("Enter a number: ")
                number = input("(Y/N): ")
                if number.isdigit():
                    number = int(number)
                else:
                    print("Invalid input.")
                    continue
                
                if number > len(numbers):
                    print("Sorry, numbers cannot be greater than the length of the list.")
                    continue
                
                if number < len(numbers):
                    numbers.append(number)
                else:
                    print("Sorry, numbers cannot be less than the length of the list.")
                    continue
                
                print("The list now contains:")
                for number in numbers:
                    print(number)
                
                print("\nWould you like to add another number? [Y/N]")
                answer = input("(Y/N): ")
                if answer.lower() == "y":
                    print("Enter a number: ")
                    number = input("(Y/N): ")
                    if number.isdigit():
                        number = int(number)
                    else:
                        print("Invalid input.")
                        continue
                
                    if number > len(numbers):
                        print("Sorry, numbers cannot be greater than the length of the list.")
                        continue
                    
                    if number < len(numbers):
                        numbers.append(number)
                    else:
                        print("Sorry, numbers cannot be less than the length of the list.")
                        continue
                
                    print("The list now contains:")
                    for number in 