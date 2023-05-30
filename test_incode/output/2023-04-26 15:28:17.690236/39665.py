#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        
        for number in numbers:
            print(number)
            
        choice = input("Enter a number to continue: ")
        
        if choice == "quit":
            break
        
        numbers.append(int(choice))
        
        print("Added number:", numbers[-1])
        
        print("Numbers:", numbers)
        
        print("Numbers sorted:", sorted(numbers))
        
        print("Numbers reversed:", reversed(numbers))
        
        print("Numbers reversed:", list(reversed(numbers)))
        
        print("Numbers reversed:", list(reversed(list(reversed(numbers))))))
        
        print("Numbers reversed:", list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(list(reversed(