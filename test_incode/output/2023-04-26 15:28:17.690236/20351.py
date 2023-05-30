#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or removes fruits. """    
    ports = input("Enter the ports separated by commas: ")
    fruits = input("Enter the fruits separated by commas: ")
    fruits = fruits.split(",")
    fruits = [x.strip() for x in fruits]
    fruits = [x for x in fruits if x != ""]
    fruits = list(set(fruits))
    fruits.sort()
    fruits = ",".join(