#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and stores user input. """    
    while True:
        words = input("Enter a list of words: ")
        words = words.split()
        
        words = [word for word in words if word not in stopwords]
        
        words = ' '.join(words)
        
        words = words.replace(' ', '')
        
        words = words.replace('\n', ' ')
        
        words = words.replace('\t', '')
        
        words = words.replace('\r', '')
        
        words = words.replace(',', '')
        
        words = words.replace('!', '')
        
        words = words.replace('?', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = words.replace('"', '')
        
        words = words.replace('(', '')
        
        words = words.replace(')', '')
        
        words = words.replace(',', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = words.replace('"', '')
        
        words = words.replace('(', '')
        
        words = words.replace(')', '')
        
        words = words.replace(',', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = words.replace('"', '')
        
        words = words.replace('(', '')
        
        words = words.replace(')', '')
        
        words = words.replace(',', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = words.replace('"', '')
        
        words = words.replace('(', '')
        
        words = words.replace(')', '')
        
        words = words.replace(',', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = words.replace('"', '')
        
        words = words.replace('(', '')
        
        words = words.replace(')', '')
        
        words = words.replace(',', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = words.replace('"', '')
        
        words = words.replace('(', '')
        
        words = words.replace(')', '')
        
        words = words.replace(',', '')
        
        words = words.replace(':', '')
        
        words = words.replace(';', '')
        
        words = words.replace('\'', '')
        
        words = 