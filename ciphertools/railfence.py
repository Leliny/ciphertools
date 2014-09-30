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


def railfence_decrypt(cipher, num_rails):
  rails = [[None for _ in xrange(len(cipher))] for _ in xrange(num_rails)]
  col = 0

  # Construct rails
  for rail in xrange(num_rails):
    if rail == 0 or rail == num_rails - 1:
      pos = (num_rails - 1) * 2
    else:
      pos = 2 * rail

    even = False
    pos = 0 if rail == 0 else pos / 2

    while pos < len(cipher):
      if col == len(cipher):
        break

      rails[rail][pos] = cipher[col]
      col += 1

      if rail == 0 or rail == num_rails - 1:
        pos += (num_rails - 1) * 2
      else:
        pos += 2 * rail if even else 2 * (num_rails - 1 - rail)

      even = not even

  # Read the message from the rails
  plain = []
  row = 0
  col = 0
  delta = 1
  while len(plain) < len(cipher):
    plain.append(rails[row][col])
    col += 1
    if row >= num_rails - 1:
      delta = -1
    elif row < 1:
      delta = 1
    row += delta

  return ''.join(plain)
