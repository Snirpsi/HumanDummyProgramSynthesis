#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and iterates over numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        for number in numbers:
            print(number)
        
        choice = input("Enter a number or q to quit: ")
        if choice == 'q':
            break
        elif choice == '1':
            numbers.append(1)
        elif choice == '2':
            numbers.append(2)
        elif choice == '3':
            numbers.append(3)
        elif choice == '4':
            numbers.append(4)
        elif choice == '5':
            numbers.append(5)
        elif choice == '6':
            numbers.append(6)
        elif choice == '7':
            numbers.append(7)
        elif choice == '8':
            numbers.append(8)
        elif choice == '9':
            numbers.append(9)
        elif choice == '10':
            numbers.append(10)
        else:
            print("Invalid choice, please try again.")
            
    print("Done.")
    
    
