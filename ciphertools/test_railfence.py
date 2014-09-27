from unittest import TestCase

from railfence import railfence_encrypt


class TestPlayfair(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hello how are you today', 'howeudel o r o oalhayty', 3)
    ]

  def test_encrypt(self):
    for plain, cipher, rails in self.ciphers:
      enc = railfence_encrypt(plain, rails)
      self.assertEqual(cipher, enc)
