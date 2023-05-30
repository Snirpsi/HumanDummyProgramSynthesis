#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests words.
    while True:
        print(random.choice(words))
        time.sleep(1)

