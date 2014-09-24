from unittest import TestCase

from scytale import scytale_decrypt, scytale_encrypt


class TestScytale(TestCase):
  def setUp(self):
    self.ciphers = [
      ('helpmeiamunderattack', 'henteidtlaeapmrcmuak', 5),
      ('hellohowareyou', 'hheeoylwolauor+', 5)
    ]

  def test_encrypt(self):
    for plain, cipher, cols in self.ciphers:
      enc = scytale_encrypt(plain, cols, padding='+')
      self.assertEqual(cipher, enc)

  def test_decrypt(self):
    for plain, cipher, cols in self.ciphers:
      dec = scytale_decrypt(cipher, cols)
      self.assertIn(plain, dec)
