from unittest import TestCase

from vigenere import vigenere_decrypt, vigenere_encrypt


class TestVigenere(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hello how are you today', 'sixzb ssioe pcaig zhmm', 'lemon')
    ]

  def test_encrypt(self):
    for plain, cipher, key in self.ciphers:
      enc = vigenere_encrypt(plain, key)
      self.assertEqual(enc, cipher)

  def test_decrypt(self):
    for plain, cipher, key in self.ciphers:
      dec = vigenere_decrypt(cipher, key)
      self.assertEqual(dec, plain.replace(' ', ''))
