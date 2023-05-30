#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and calculates fruits. """    
    
    words = []
    fruits = []
    
    while True:
        
        line = input('Enter a word: ')
        
        if line == 'quit':
            break
        
        words.append(line)
        
        fruits.append(len(set(words)))
        
        print('The word ' + line + ' has ' + str(fruits[-1]) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(len(set(words))) + ' unique words.')
        
        print('The word ' + line + ' has ' + str(sum(1 for _ in words)) + ' words.')
        
        print('The word ' + line + ' has ' + str(sum(1 for _ in fruits)) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)/len(fruits)) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)/len(fruits)*100) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)/len(fruits)*100/len(fruits)) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)/len(fruits)*100/len(fruits)*100) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)) + ' fruits.')
        
        print('The word ' + line + ' has ' + str(sum(fruits)/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100/len(fruits)*100