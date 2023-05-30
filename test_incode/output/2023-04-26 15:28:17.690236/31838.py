#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates fruits. """    
    fruits = calculate_fruits()
    
    # Print the fruits in the order they were calculated.
    for fruit in fruits:
        print(fruit)
    
    # Print the total amount of fruits.
    print("Total amount of fruits: {}".format(sum(fruits)))
    
    # Print the amount of apples.
    print("Total amount of apples: {}".format(sum(fruits['apples'])))
    
    # Print the amount of oranges.
    print("Total amount of oranges: {}".format(sum(fruits['oranges'])))
    
    # Print the amount of pears.
    print("Total amount of pears: {}".format(sum(fruits['pears'])))
    
    # Print the amount of bananas.
    print("Total amount of bananas: {}".format(sum(fruits['bananas'])))
    
    # Print the amount of kiwis.
    print("Total amount of kiwis: {}".format(sum(fruits['kiwis'])))
    
    # Print the amount of grapes.
    print("Total amount of grapes: {}".format(sum(fruits['grapes'])))
    
    # Print the amount of watermelons.
    print("Total amount of watermelons: {}".format(sum(fruits['watermelons'])))
    
    # Print the amount of grapefruits.
    print("Total amount of grapefruits: {}".format(sum(fruits['grapefruits'])))
    
    # Print the amount of mangoes.
    print("Total amount of mangoes: {}".format(sum(fruits['mangoes'])))
    
    # Print the amount of bananas, and print a message saying how many of them are bananas.
    print("Total amount of bananas: {}".format(sum(fruits['bananas'])))
    print("Total amount of bananas: {}".format(len(fruits['bananas'])))
    
    # Print the amount of apples, and print a message saying how many of them are apples.
    print("Total amount of apples: {}".format(sum(fruits['apples'])))
    print("Total amount of apples: {}".format(len(fruits['apples'])))
    
    # Print the amount of oranges, and print a message saying how many of them are oranges.
    print("Total amount of oranges: {}".format(sum(fruits['oranges'])))
    print("Total amount of oranges: {}".format(len(fruits['oranges'])))
    
    # Print the amount of pears, and print a message saying how many of them are pears.
    print("Total amount of pears: {}".format(sum(fruits['pears'])))
    print("Total amount of pears: {}".format(len(fruits['pears'])))
    
    # Print the amount of kiwis, and print a 