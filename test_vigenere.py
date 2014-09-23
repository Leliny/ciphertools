from unittest import TestCase

from vigenere import vigenere_decrypt, vigenere_encrypt


class TestVigenere(TestCase):
  def setUp(self):
    self.PLAIN = 'hello how are you today'
    self.CIPHER = 'sixzb ssioe pcaig zhmm'
    self.KEY = 'lemon'

  def test_encrypt(self):
    enc = vigenere_encrypt(self.PLAIN, self.KEY)
    self.assertEqual(enc, self.CIPHER)

  def test_decrypt(self):
    dec = vigenere_decrypt(self.CIPHER, self.KEY)
    self.assertEqual(dec, self.PLAIN.replace(' ', ''))
