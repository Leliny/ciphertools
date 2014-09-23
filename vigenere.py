from itertools import cycle
import string

def vigenere_encrypt(plain, key):
  """ Vigenere encrypts plaintext with key. """
  plain = plain.lower()
  key = key.lower()
  alphabet = string.ascii_lowercase
  def enc_char(p, k):
    if p not in alphabet:
      return p
    c = alphabet.find(p) + alphabet.find(k)
    return alphabet[c % len(alphabet)]
  zipped = zip(plain.replace(' ', ''), cycle(key))
  cipher = ''.join([enc_char(p,k) for p,k in zipped])
  return ' '.join([cipher[i:i+5] for i in xrange(0, len(cipher), 5)])

def vigenere_decrypt(cipher, key):
  """ Vigenere decrypts plaintext with key. """
  cipher = cipher.lower()
  key = key.lower()
  alphabet = string.ascii_lowercase
  def dec_char(c, k):
    if c not in alphabet:
      return c
    p = (alphabet.find(c) - alphabet.find(k)) + len(alphabet)
    return alphabet[p % len(alphabet)]
  zipped = zip(cipher.replace(' ', ''), cycle(key))
  return ''.join([dec_char(c,k) for c,k in zipped])

