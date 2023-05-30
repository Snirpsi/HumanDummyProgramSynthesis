#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and calculates words. """    
    
    # Read input from stdin
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    # Remove words and calculate their frequencies
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    # Print the results
    for word, frequency in word_frequencies.items():
        print('%s: %d' % (word, frequency))
    
    # Print the final result
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total words: %d' % len(word_frequencies))
    print('Average word length: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Average word frequency: %.2f' % float(sum(word_frequencies.values())) / len(word_frequencies))
    print('Total word