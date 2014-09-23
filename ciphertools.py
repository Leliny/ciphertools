#!/usr/bin/env python

import string

def caesar(s, shift):
  s = s.lower()
  letters = string.ascii_lowercase
  def shift_char(c):
    if c not in letters:
      return c
    idx = letters.find(c)
    return letters[(idx + shift) % len(letters)]
  return ''.join([shift_char(c) for c in s])

def caesar_solve(s):
  def score(shift, words):
    decrypted = caesar(s, shift)
    score = 0
    decrypted_words = decrypted.split(' ')
    score = sum([len(word) for word in decrypted_words if word in words])
    return (decrypted, score)
  with open('/usr/share/dict/words', 'r') as wordfile:
    words = [w.lower() for w in wordfile.read().split('\n')]
    results = []
    for shift in xrange(26):
      results.append(score(shift, words))
    results.sort(key=lambda((decrypted, score)): score, reverse=True)
    return [decrypted for (decrypted, score) in results]

