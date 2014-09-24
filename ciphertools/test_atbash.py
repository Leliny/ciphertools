from unittest import TestCase

from atbash import atbash_decrypt, atbash_encrypt


class TestAtbash(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hello how are you today?', 'svool sld ziv blf glwzb?'),
      ('abcdefhijklmnopqrstuvwxyz', 'zyxwvusrqponmlkjihgfedcba')
    ]

  def test_encrypt(self):
    for plain, cipher in self.ciphers:
      enc = atbash_encrypt(plain)
      self.assertEqual(cipher, enc)

  def test_decrypt(self):
    for plain, cipher in self.ciphers:
      dec = atbash_decrypt(cipher)
      self.assertEqual(plain, dec)
