import english_words

DICT_WORDS = english_words.get_words()

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
  def score(dist, offset):
    decrypted = skip(s, dist, offset=offset)
    decrypted_words = decrypted.split(' ')
    result = sum([len(word) for word in decrypted_words if word in DICT_WORDS])
    return (decrypted, result)
  results = []
  for offset in xrange(len(s)):
    for dist in xrange(max_dist):
      decrypted, cur_score = score(dist, offset)
      results.append((decrypted, cur_score))
      # Break if all words are in the dictionary
      if cur_score == len(s.replace(' ', '')):
        return [decrypted]
  results.sort(key=lambda((decrypted, score)): score, reverse=True)
  return [decrypted for (decrypted, score) in results]

