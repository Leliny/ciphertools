from unittest import TestCase

from playfair import playfair_decrypt, playfair_encrypt


class TestPlayfair(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hide the gold in the tree stump', 'bmodzbxdnabekudmuixmmouvif', 'playfair example'),
    ]

  def test_encrypt(self):
    for plain, cipher, key in self.ciphers:
      enc = playfair_encrypt(plain, key)
      self.assertEqual(cipher, enc)

  def test_decrypt(self):
    for plain, cipher, key in self.ciphers:
      dec = playfair_decrypt(cipher, key)
      self.assertEqual(plain, dec)
