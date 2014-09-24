import string


def _construct_grid(key):
  key = [c for c in key.lower()]
  result = []
  letters = set([c for c in string.ascii_lowercase if c != 'j'])

  for c in key:
    if c in letters:
      result.append(c)
      letters.remove(c)

  for c in sorted(letters):
    result.append(c)

  # Transform into grid
  return [result[i:i + 5] for i in range(0, len(result), 5)]


def playfair_encrypt(plain, key, padding='x'):
  padding = padding.lower()
  plain = plain.replace('j', 'i')
  plain = [c for c in plain.lower() if c in string.ascii_lowercase]
  grid = _construct_grid(key)

  idx = 0
  while idx < len(plain):
    digraph = plain[idx:idx + 2]
    if len(digraph) == 1:
      plain.append(padding)
      idx = 0
    elif digraph[0] == digraph[1]:
      plain.insert(idx + 1, padding)
      idx = 0
    else:
      idx += 2

  digraphs = [''.join(plain[idx:idx + 2]) for idx in range(0, len(plain), 2)]

  def encrypt_lookup(di):
    i1, j1 = None, None
    i2, j2 = None, None
    for i in xrange(5):
      for j in xrange(5):
        if grid[i][j] == di[0]:
          i1, j1 = i, j
        elif grid[i][j] == di[1]:
          i2, j2 = i, j

    if i1 == i2:
      # Same row
      return grid[i1][(j1 + 1) % 5] + grid[i1][(j2 + 1) % 5]
    elif j1 == j2:
      # Same column
      return grid[(i1 + 1) % 5][j1] + grid[(i2 + 1) % 5][j1]
    else:
      # Form a rectangle
      return grid[i1][j2] + grid[i2][j1]

  return ''.join([encrypt_lookup(digraph) for digraph in digraphs])


def playfair_decrypt(cipher, key):
  grid = _construct_grid(key)
  cipher = cipher.lower().replace('j', 'i')
  cipher = [c for c in cipher]

  def decrypt_lookup(di):
    i1, j1 = None, None
    i2, j2 = None, None
    for i in xrange(5):
      for j in xrange(5):
        if grid[i][j] == di[0]:
          i1, j1 = i, j
        elif grid[i][j] == di[1]:
          i2, j2 = i, j

    if i1 == i2:
      # Same row
      return grid[i1][(j1 - 1) % 5] + grid[i1][(j2 - 1) % 5]
    elif j1 == j2:
      # Same column
      return grid[(i1 - 1) % 5][j1] + grid[(i2 - 1) % 5][j1]
    else:
      # Form a rectangle
      return grid[i1][j2] + grid[i2][j1]

  digraphs = [''.join(cipher[idx:idx + 2]) for idx in range(0, len(cipher), 2)]
  return ''.join([decrypt_lookup(digraph) for digraph in digraphs])
