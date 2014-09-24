ciphertools
===========

A python file with common cipher functions.

Installation
------------

```sh
git clone https://github.com/avp/ciphertools
cd ciphertools
./setup.py install
```

Usage
-----

```python
from ciphertools import playfair
ciphered = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(ciphered, key)
```

Supported Ciphers
-----------------

- Caesar
- Atbash
- Skip
- Playfair
- Vigenere
- Scytale
- More to be added soon
