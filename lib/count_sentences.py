#!/usr/bin/env python3

class MyString:
  def __init__(self,value):
    if not isinstance(value,str):
      raise ValueError("The Value must be a string.")
    self._value = value

  #get method
  def value(self):
    return self._value

  def is_sentence(self):
    return self._value.endswith('.')
  
  def is_question(self):
    return self._value.endswith('?')
  
  def is_exclamation(self):
    return self._value.endswith('!')
  
  def count_sentences(self):
        count = 0
        for sentence in self._value:
            if sentence.endswith('.') or sentence.endswith('!') or sentence.endswith('?'):
                count += 1
        return count