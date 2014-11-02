import english_words

DICT_WORDS = english_words.get_words()


def skip(plain, dist, offset=0):
  """ Skip cipher the string plain by an amount dist starting at offset """
  idx = offset % len(plain)
  result = []
  while len(result) < len(plain):
    result.append(plain[idx])
    idx = (idx + dist) % len(plain)
  return ''.join(result)


def _score(cipher, dist, offset):
  dec = skip(cipher, dist, offset=offset)
  dec_words = dec.split(' ')
  result = sum([len(word) for word in dec_words if word in DICT_WORDS])
  return dec, result


def skip_solve(cipher, max_dist=None):
  """ Solve a Skip cipher by checking in a dictionary
  Returns a list of the possible decrypted strings with most likely first.
  """
  max_dist = max_dist if max_dist is not None else len(cipher)

  results = []
  for offset in xrange(len(cipher)):
    for dist in xrange(max_dist):
      decrypted, cur_score = _score(cipher, dist, offset)
      results.append((decrypted, cur_score))
      # Break if all words are in the dictionary
      if cur_score == len(cipher.replace(' ', '')):
        return [decrypted]
  results.sort(key=lambda ((_, s)): s, reverse=True)
  return [d for (d, _) in results]
