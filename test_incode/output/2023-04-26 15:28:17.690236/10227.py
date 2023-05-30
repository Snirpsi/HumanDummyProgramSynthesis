#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and stores fruits. """    
    
    words = []
    
    while True:
        
        fruits = input("Enter a fruit (case insensitive): ")
        
        if fruits == "":
            
            break
        
        fruits = fruits.lower()
        
        if fruits not in words:
            
            words.append(fruits)
            
        else:
            
            print("That fruit already exists. Try again.")
            
    
    print("\nThe list of words is:")
    
    for word in words:
        
        print(word)
    
    print("\nThe total fruit count is:", len(words))
    
    print("\nThe fruit count is:", len(set(words)))
    
    print("\nThe average fruit count is:", len(words)/len(words))
    
    print("\nThe average fruit count is:", len(words)/len(set(words)))
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100)
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(words))
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100)
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100/len(words))
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100/len(set(words))*100)
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(words))
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(set(words))*100)
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(set(words))*100)
    
    print("\nThe average fruit count is:", len(words)/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(set(words))*100/len(set(words))*100)
    
    print("\nThe average fruit count is:", len(words)/