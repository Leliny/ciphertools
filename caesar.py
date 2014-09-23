import string

import english_words

DICT_WORDS = english_words.get_words()

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
  def score(shift):
    decrypted = caesar(s, shift)
    score = 0
    decrypted_words = decrypted.split(' ')
    score = sum([len(word) for word in decrypted_words if word in DICT_WORDS])
    return (decrypted, score)
  results = [score(shift) for shift in xrange(26)]
  results.sort(key=lambda((decrypted, score)): score, reverse=True)
  return [decrypted for (decrypted, score) in results]

