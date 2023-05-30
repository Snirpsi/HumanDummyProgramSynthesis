#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    
    # Create a fruit-store object
    fruitStore = FruitStore()
    
    # Add some fruits to the store
    fruitStore.addFruit("apple")
    fruitStore.addFruit("banana")
    fruitStore.addFruit("cherry")
    
    # Print the fruits in the store
    fruits = fruitStore.getFruits()
    print("There are {0} fruits.".format(len(fruits)))
    
    # Print the fruit with the lowest price
    lowestPrice = fruitStore.getLowestPrice()
    print("The lowest price is $ {0}".format(lowestPrice))
    
    # Print the fruit with the highest price
    highestPrice = fruitStore.getHighestPrice()
    print("The highest price is $ {0}".format(highestPrice))
    
    # Print the fruit with the lowest price and highest price
    lowestPriceAndHighestPrice = fruitStore.getLowestPriceAndHighestPrice()
    print("The lowest price is $ {0}".format(lowestPriceAndHighestPrice[0]))
    print("The highest price is $ {0}".format(lowestPriceAndHighestPrice[1]))
    
    # Print the fruit with the lowest price and highest price and their price
    lowestPriceAndHighestPriceAndPrice = fruitStore.getLowestPriceAndHighestPriceAndPrice()
    print("The lowest price is $ {0}".format(lowestPriceAndHighestPriceAndPrice[0]))
    print("The highest price is $ {0}".format(lowestPriceAndHighestPriceAndPrice[1]))
    
    # Print the fruit with the lowest price and highest price and their price and their price
    lowestPriceAndHighestPriceAndPriceAndPrice = fruitStore.getLowestPriceAndHighestPriceAndPriceAndPrice()
    print("The lowest price is $ {0}".format(lowestPriceAndHighestPriceAndPriceAndPrice[0]))
    print("The highest price is $ {0}".format(lowestPriceAndHighestPriceAndPriceAndPrice[1]))
    
    # Print the fruit with the lowest price and highest price and their price and their price and their price
    lowestPriceAndHighestPriceAndPriceAndPriceAndPrice = fruitStore.getLowestPriceAndHighestPriceAndPriceAndPriceAndPrice()
    print("The lowest price is $ {0}".format(lowestPriceAndHighestPriceAndPriceAndPriceAnd