import string

import english_words

DICT_WORDS = english_words.get_words()


def caesar(plain, shift):
  """ Shift the string plain by an amount shift """
  plain = plain.lower()
  letters = string.ascii_lowercase

  def shift_char(char):
    if char not in letters:
      return char
    idx = letters.find(char)
    return letters[(idx + shift) % len(letters)]

  return ''.join([shift_char(c) for c in plain])


def caesar_solve(cipher):
  """ Solve a Caesar cipher by checking in a dictionary.
  Returns a list of the possible decrypted strings with most likely first.
  """

  def score(shift):
    decrypted = caesar(cipher, shift)
    decrypted_words = decrypted.split(' ')
    result = sum([len(word) for word in decrypted_words if word in DICT_WORDS])
    return decrypted, result

  results = [score(sh) for sh in xrange(26)]
  results.sort(key=lambda ((_, sc)): sc, reverse=True)
  return [d for (d, _) in results]

