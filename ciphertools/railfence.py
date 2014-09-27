def railfence_encrypt(plain, num_rails):
  plain = [c.lower() for c in plain]
  rails = [[] for _ in xrange(num_rails)]
  row_idx = 0
  delta = 1
  for c in plain:
    rails[row_idx].append(c)
    if row_idx >= num_rails - 1:
      delta = -1
    elif row_idx < 1:
      delta = 1
    row_idx += delta
  return ''.join([''.join(rail) for rail in rails])
