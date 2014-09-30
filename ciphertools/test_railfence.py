from unittest import TestCase

from railfence import railfence_encrypt, railfence_decrypt


class TestRailfence(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hello how are you today', 'howeudel o r o oalhayty', 3)
    ]

  def test_encrypt(self):
    for plain, cipher, rails in self.ciphers:
      enc = railfence_encrypt(plain, rails)
      self.assertEqual(cipher, enc)

  def test_decrypt(self):
    for plain, cipher, rails in self.ciphers:
      dec = railfence_decrypt(cipher, rails)
      self.assertEqual(plain, dec)
