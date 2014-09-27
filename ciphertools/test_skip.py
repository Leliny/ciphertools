from unittest import TestCase

from skip import skip, skip_solve


class TestSkip(TestCase):
  def setUp(self):
    self.ciphers = [
      ('hello how are you today', 'h aodloe yo yoehrualw t', 5),
    ]

  def test_skip(self):
    for plain, cipher, shift in self.ciphers:
      enc = skip(plain, 5)
      self.assertEqual(cipher, enc)

  def test_skip_solve(self):
    for plain, cipher, _ in self.ciphers:
      dec = skip_solve(cipher)
      self.assertEqual(plain, dec[0])
