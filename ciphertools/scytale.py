import math


def scytale_encrypt(plain, cols, padding=' '):
  rows = int(math.ceil(len(plain) / float(cols)))
  chunks = []
  for i in xrange(rows):
    chunk = [c for c in plain[i * cols:(i * cols) + cols]]
    chunk += [padding] * (cols - len(chunk))
    chunks.append(tuple(chunk))
  result = [''.join([t[i] for t in chunks]) for i in xrange(cols)]
  return ''.join(result)


def scytale_decrypt(cipher, cols):
  rows = int(math.ceil(len(cipher) / float(cols)))
  result = [cipher[i::rows] for i in xrange(rows)]
  return ''.join(result)
