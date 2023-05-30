#!/usr/bin/python3
if __name__ == '__main__':
    #A function that calculates user input.
    #It takes two arguments: a string and a number.
    #It returns the string with the number replaced by the string argument.
    #If the number is a negative number, the function returns an empty string.
    #If the number is a positive number, the function returns the string with the number replaced by the string argument.
    #If the number is 0, the function returns an empty string.
    #If the number is greater than the length of the string, it returns an empty string.
    #If the number is less than the length of the string, it returns an empty string.
    
    #Get the user input from the user.
    number = int(input("Enter a number: "))
    string = input("Enter a string: ")
    
    #If the number is negative, return an empty string.
    if number < 0:
        return ""
    
    #If the number is positive, return the string with the number replaced by the string argument.
    elif number > 0:
        return string.replace(str(number), string)
    
    #If the number is 0, return an empty string.
    elif number == 0:
        return ""
    
    #If the number is greater than the length of the string, return an empty string.
    elif number > len(string):
        return ""
    
    #If the number is less than the length of the string, return an empty string.
    elif number < len(string):
        return string.replace(str(number), "")
    
    #If the number is greater than the length of the string, return an empty string.
    else:
        return string
    
    #If the number is greater than the length of the string, return an empty string.
    else:
        return string

