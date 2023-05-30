#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and removes a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_to_remove = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Open the file that contains the list of numbers to remove.
    with open("numbers_to_remove.txt", "r") as file:
        numbers_to_remove = file.readlines()
    
    # Remove each number from the list.
    for number in numbers_to_remove:
        numbers.remove(number)
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
    
    # Close the file.
    file.close()
    
    # Print the list to stdout.
    print("Removed " + str(len(numbers)) + " numbers from list")
