#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and adds words. """    
    
    numbers = []
    words = []
    
    while True:
        numbers.append(input("Enter a number: "))
        words.append(input("Enter a word: "))
        
        if len(words) == 3:
            break
    
    print("The numbers are:")
    print(numbers)
    print("The words are:")
    print(words)
    
    print("The sum of the numbers is ", sum(numbers))
    print("The sum of the words is ", sum(words))
    
    print("The average of the numbers is ", sum(numbers)/len(numbers))
    print("The average of the words is ", sum(words)/len(words))
    
    print("The maximum of the numbers is ", max(numbers))
    print("The maximum of the words is ", max(words))
    
    print("The minimum of the numbers is ", min(numbers))
    print("The minimum of the words is ", min(words))
    
    print("The standard deviation of the numbers is ", 
          math.sqrt((sum(numbers)-sum(numbers)*len(numbers))/len(numbers))
          )
    print("The standard deviation of the words is ", 
          math.sqrt((sum(words)-sum(words*len(words))/len(words))
          )
          )
    
    print("The variance of the numbers is ", 
          math.sqrt((sum(numbers)-sum(numbers)*len(numbers))/len(numbers))
          )
    print("The variance of the words is ", 
          math.sqrt((sum(words)-sum(words*len(words))/len(words))
          )
          )
    
    print("The skewness of numbers is ", 
          math.sqrt((sum(numbers)-sum(numbers)*len(numbers))/len(numbers))
          )
    print("The skewness of words is ", 
          math.sqrt((sum(words)-sum(words*len(words))/len(words))
          )
          )
    
    print("The kurtosis of numbers is ", 
          math.sqrt((sum(numbers)-sum(numbers)*len(numbers))/len(numbers))
          )
    print("The kurtosis of words is ", 
          math.sqrt((sum(words)-sum(words*len(words))/len(words))
          )
          )
    
    print("The skewness of the numbers is ", 
          math.sqrt((sum(numbers)-sum(numbers)*len(numbers))/len(numbers))
          )
    print("The skewness of the words is ", 
          math.sqrt((sum(words)-sum(words*len(words))/len(words))
          )
          )
    
    print("The kurtosis of the numbers is ", 
          math.sqrt((sum(numbers)