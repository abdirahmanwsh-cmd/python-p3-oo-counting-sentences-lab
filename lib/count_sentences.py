#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace punctuation with periods for consistent splitting
        text = self.value.replace('!', '.').replace('?', '.')
        # Split by periods and filter out empty strings
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return len(sentences)