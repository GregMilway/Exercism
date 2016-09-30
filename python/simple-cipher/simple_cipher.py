#implement a simple shift cipher, using lower case letters.
#implement a Caesar cipher, with key = 'd'
from random import choice
from string import ascii_lowercase
import re

class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = self.gen_key()
        elif not key.islower() or not key.isalpha():
            raise ValueError('Key must be lower-case ascii letters [a-z]')
        self.key = key

    def gen_key(self):
        return ''.join(choice(ascii_lowercase) for _ in xrange(100))

    def encode(self,plaintext):
        plaintext = re.sub('[^A-Za-z]','',plaintext.lower())
        key = self._get_key(len(plaintext))
        return ''.join(self._shift(key[i],txtchar,'e') for i, txtchar in enumerate(plaintext))

    def decode(self,ciphertext):
        key = self._get_key(len(ciphertext))
        return ''.join(self._shift(key[i],txtchar,'d') for i, txtchar in enumerate(ciphertext))

    def _get_key(self,length):
        key = self.key
        if len(key) < length:
            key *= int(length / len(key)) + 1
        return key

    def _shift(self,keychar,txtchar,mode):
        keyint = ord(keychar) - 97
        txtint = ord(txtchar) - 97
        if mode == 'e':
            return chr( (txtint + keyint)%26 + 97)
        elif mode == 'd':
            return chr( (txtint - keyint)%26 + 97)

class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self,'d')
