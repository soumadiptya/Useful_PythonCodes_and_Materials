# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:39:59 2021

@author: souma
"""
# Expected output
# my_sentence = Sentence('This is a test')
# for word in my_sentence:
#     print(word)

# First we have to create a sentence class
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence 
        self.index = 0
        self.words = self.sentence.split()
        self.length = len(self.words)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        current = self.words[self.index]
        self.index += 1
        return current

my_sentence = Sentence('This is a test')
for word in my_sentence:
    print(word)
# Generator for the same
def sentence_generator(sentence):
    for word in sentence.split():
        yield word
sentence_gen = sentence_generator("This is a test")
for word in sentence_gen:
    print(word)
print(next(sentence_gen)) # Gives StopIteration
