#!/usr/bin/env python3

import random

word_file = open('english.words')
words = {word[:-1] for word in word_file}
word_file.close()

def babble():
    length = random.randint(1, 16)
    word = ''.join([chr(ord('a')+random.randint(0, 25)) for i in range(length)])
    return word

count = 0
fake_words = set()
while count < 10000:
    word = babble()
    if word in words or word in fake_words:
        continue
    count += 1
    fake_words |= {word}

for word in fake_words:
    print(word)
