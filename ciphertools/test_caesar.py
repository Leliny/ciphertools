from unittest import TestCase

from caesar import caesar, caesar_solve


class TestCaesar(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hello how are you today?', 'mjqqt mtb fwj dtz ytifd?', 5)
    ]

  def test_caesar(self):
    for plain, cipher, shift in self.ciphers:
      enc = caesar(plain, 5)
      self.assertEqual(cipher, enc)

  def test_caesar_solve(self):
    for plain, cipher, _ in self.ciphers:
      dec = caesar_solve(cipher)
      self.assertEqual(plain, dec[0])
