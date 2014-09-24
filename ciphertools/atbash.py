import string


def _convert_char(c):
  letters = string.ascii_lowercase
  return letters[len(letters) - 1 - letters.find(c)] if c in letters else c


def atbash_encrypt(plain):
  plain = plain.lower()
  return ''.join([_convert_char(c) for c in plain])


def atbash_decrypt(cipher):
  """ Atbash decryption is equivalent to decryption """
  return atbash_encrypt(cipher)
