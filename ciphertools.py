#!/usr/bin/env python

import string

DICT_PATH = '/usr/share/dict/words'

def caesar(s, shift):
  """ Shift the string s by an amount shift """
  s = s.lower()
  letters = string.ascii_lowercase
  def shift_char(c):
    if c not in letters:
      return c
    idx = letters.find(c)
    return letters[(idx + shift) % len(letters)]
  return ''.join([shift_char(c) for c in s])

def caesar_solve(s):
  """ Solve a Caesar cipher by checking in a dictionary
  Returns a list of the possible decrypted strings with most likely first.
  """
  with open(DICT_PATH, 'r') as wordfile:
    words = [w.strip().lower() for w in wordfile.readlines()]
  def score(shift):
    decrypted = caesar(s, shift)
    score = 0
    decrypted_words = decrypted.split(' ')
    score = sum([len(word) for word in decrypted_words if word in words])
    return (decrypted, score)
  results = [score(shift) for shift in xrange(26)]
  results.sort(key=lambda((decrypted, score)): score, reverse=True)
  return [decrypted for (decrypted, score) in results]

def skip(s, dist, offset=0):
  """ Skip cipher the string s by an amount dist starting at offset """
  idx = offset % len(s)
  result = []
  while len(result) < len(s):
    result.append(s[idx])
    idx = (idx + dist) % len(s)
  return ''.join(result)

def skip_solve(s, max_dist=None):
  """ Solve a Skip cipher by checking in a dictionary
  Returns a list of the possible decrypted strings with most likely first.
  """
  max_dist = max_dist if max_dist is not None else len(s)
  with open(DICT_PATH, 'r') as wordfile:
    words = [w.strip().lower() for w in wordfile.readlines()]
  def score(dist, offset):
    decrypted = skip(s, dist, offset)
    score = 0
    decrypted_words = decrypted.split(' ')
    score = sum([len(word) for word in decrypted_words if word in words])
    return (decrypted, score)
  results = []
  for offset in xrange(len(s)):
    for dist in xrange(max_dist):
      decrypted, cur_score = score(dist, offset)
      results.append((decrypted, cur_score))
      # Break if all words are in the dictionary
      if cur_score == len(s.replace(' ', '')):
        break
  results.sort(key=lambda((decrypted, score)): score, reverse=True)
  return [decrypted for (decrypted, score) in results]

