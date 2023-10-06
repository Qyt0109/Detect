"""SYMMETRIC KEY CRYPTOGRAPHY (SKC)
 .d8888b.    Y88b   d88P   888b     d888   888b     d888   8888888888   88888888888   8888888b.    8888888    .d8888b.          888    d8P    8888888888   Y88b   d88P 
d88P  Y88b    Y88b d88P    8888b   d8888   8888b   d8888   888              888       888   Y88b     888     d88P  Y88b         888   d8P     888           Y88b d88P  
Y88b.          Y88o88P     88888b.d88888   88888b.d88888   888              888       888    888     888     888    888         888  d8P      888            Y88o88P   
 "Y888b.        Y888P      888Y88888P888   888Y88888P888   8888888          888       888   d88P     888     888                888d88K       8888888         Y888P    
    "Y88b.       888       888 Y888P 888   888 Y888P 888   888              888       8888888P"      888     888                8888888b      888              888     
      "888       888       888  Y8P  888   888  Y8P  888   888              888       888 T88b       888     888    888         888  Y88b     888              888     
Y88b  d88P       888       888   "   888   888   "   888   888              888       888  T88b      888     Y88b  d88P         888   Y88b    888              888     
 "Y8888P"        888       888       888   888       888   8888888888       888       888   T88b   8888888    "Y8888P"          888    Y88b   8888888888       888     
                                                                                                                                                                       
                                                                                                                                                                       
                                                                                                                                                                       
     .d8888b.    8888888b.    Y88b   d88P   8888888b.    88888888888    .d88888b.     .d8888b.    8888888b.           d8888   8888888b.    888    888   Y88b   d88P    
    d88P  Y88b   888   Y88b    Y88b d88P    888   Y88b       888       d88P" "Y88b   d88P  Y88b   888   Y88b         d88888   888   Y88b   888    888    Y88b d88P     
    888    888   888    888     Y88o88P     888    888       888       888     888   888    888   888    888        d88P888   888    888   888    888     Y88o88P      
    888          888   d88P      Y888P      888   d88P       888       888     888   888          888   d88P       d88P 888   888   d88P   8888888888      Y888P       
    888          8888888P"        888       8888888P"        888       888     888   888  88888   8888888P"       d88P  888   8888888P"    888    888       888        
    888    888   888 T88b         888       888              888       888     888   888    888   888 T88b       d88P   888   888          888    888       888        
    Y88b  d88P   888  T88b        888       888              888       Y88b. .d88P   Y88b  d88P   888  T88b     d8888888888   888          888    888       888        
     "Y8888P"    888   T88b       888       888              888        "Y88888P"     "Y8888P88   888   T88b   d88P     888   888          888    888       888        
"""

from abc import abstractmethod
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from SecurityScheme.Cryptography.CommonHelper.validation import check_length, check_none, check_type

"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        AES                         ┃
┣━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━┫
┃    ┃          ┃  SPECIAL   ┃ PARALLELABLE  ┃RANDOM ┃
┃MODE┃PARAMETERS┃REQUIREMENTS┣━━━━━━━┳━━━━━━━┫ READ  ┃
┃    ┃          ┃            ┃ENCRYPT┃DECRYPT┃ACCESS ┃
┣━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫
┃    ┃          ┃            ┃       ┃       ┃       ┃
┃ECB ┃Key       ┃Padding     ┃  YES  ┃  YES  ┃  YES  ┃
┃    ┃          ┃            ┃       ┃       ┃       ┃
┣━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫
┃    ┃          ┃            ┃       ┃       ┃       ┃
┃CTR ┃Key, Nonce┃No          ┃  YES  ┃  YES  ┃  YES  ┃
┃    ┃          ┃            ┃       ┃       ┃       ┃
┣━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫
┃    ┃          ┃            ┃       ┃       ┃       ┃
┃CBC ┃Key, IV   ┃Padding     ┃  NO   ┃  NO   ┃  NO   ┃
┃    ┃          ┃            ┃       ┃       ┃       ┃
┗━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━┻━━━━━━━┻━━━━━━━┛
* Padding, IV size = AES block size = 16 bytes. Nonce = 1/2 AES block size = 8 bytes
"""

AES_KEY_SIZE = 32


class AES_Cryptography:
    def __init__(self):
        self.key = None
        self.cipher = None

    def generate_key(self):
        self.key = get_random_bytes(AES_KEY_SIZE)

    def import_key(self, key: bytes):
        # Validation
        if key:
            check_type(key, bytes, "Key must be bytes")
            check_length(
                key, AES_KEY_SIZE, f"Invalid key length. Key must be {AES_KEY_SIZE} bytes.")
            self.key = key

    @abstractmethod
    def encrypt(self, plain_text: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, cipher_text: bytes) -> bytes:
        pass

    @abstractmethod
    def generate_parameters(self):
        pass

    @abstractmethod
    def import_parameters(self, key):
        pass


"""Counter (CTR)
CTR (Counter): CTR mode is a popular choice for random access and parallel processing.
It converts the block cipher into a stream cipher by using a unique counter value for each block.
CTR mode allows for encryption and decryption of blocks in parallel, making it suitable for scenarios where random access is required, such as images.
┌───────────────────────────────────────────────────────────────────────────────────────┐
│        ┌──────────┬──────────┐     ┌──────────┬──────────┐     ┌──────────┬──────────┐│
│        │  Nonce   │Counter 0 │     │  Nonce   │Counter 1 │     │  Nonce   │Counter 2 ││
│        └──────────┼──────────┘     └──────────┼──────────┘     └──────────┼──────────┘│
│                   │                           │                           │           │
│                   ▼                           ▼                           ▼           │
│    ┌───┐    ┌───────────┐      ┌───┐    ┌───────────┐      ┌───┐    ┌───────────┐     │
│    │Key├───▶│ENCRYPTION │      │Key├───▶│ENCRYPTION │      │Key├───▶│ENCRYPTION │     │
│    └───┘    └─────┬─────┘      └───┘    └─────┬─────┘      └───┘    └─────┬─────┘     │
│                   │                           │                           │           │
│                   ▼                           ▼                           ▼           │
│┌───────────┐     .─.       ┌───────────┐     .─.       ┌───────────┐     .─.          │
││ Plaintext ├───▶( X )      │ Plaintext ├───▶( X )      │ Plaintext ├───▶( X )         │
│└───────────┘     `┬'       └───────────┘     `┬'       └───────────┘     `┬'          │
│                   │                           │                           │           │
│                   ▼                           ▼                           ▼           │
│             ┌───────────┐               ┌───────────┐               ┌───────────┐     │
│             │Ciphertext │               │Ciphertext │               │Ciphertext │     │
│             └───────────┘               └───────────┘               └───────────┘     │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────────────────────────────────────┐
│        ┌──────────┬──────────┐     ┌──────────┬──────────┐     ┌──────────┬──────────┐│
│        │  Nonce   │Counter 0 │     │  Nonce   │Counter 1 │     │  Nonce   │Counter 2 ││
│        └──────────┼──────────┘     └──────────┼──────────┘     └──────────┼──────────┘│
│                   │                           │                           │           │
│                   ▼                           ▼                           ▼           │
│    ┌───┐    ┌───────────┐      ┌───┐    ┌───────────┐      ┌───┐    ┌───────────┐     │
│    │Key├───▶│ENCRYPTION │      │Key├───▶│ENCRYPTION │      │Key├───▶│ENCRYPTION │     │
│    └───┘    └─────┬─────┘      └───┘    └─────┬─────┘      └───┘    └─────┬─────┘     │
│                   │                           │                           │           │
│                   ▼                           ▼                           ▼           │
│┌───────────┐     .─.       ┌───────────┐     .─.       ┌───────────┐     .─.          │
││Ciphertext ├───▶( X )      │Ciphertext ├───▶( X )      │Ciphertext ├───▶( X )         │
│└───────────┘     `┬'       └───────────┘     `┬'       └───────────┘     `┬'          │
│                   │                           │                           │           │
│                   ▼                           ▼                           ▼           │
│             ┌───────────┐               ┌───────────┐               ┌───────────┐     │
│             │ Plaintext │               │ Plaintext │               │ Plaintext │     │
│             └───────────┘               └───────────┘               └───────────┘     │
└───────────────────────────────────────────────────────────────────────────────────────┘
"""


class AES_CTR(AES_Cryptography):
    def __init__(self):
        super().__init__()
        self.nonce = None

    def generate_nonce(self):
        self.nonce = get_random_bytes(8)

    def generate_parameters(self):
        super().generate_key()
        self.generate_nonce()

    def import_nonce(self, nonce: bytes):
        # Validation
        if nonce:
            check_type(nonce, bytes, "Nonce must be bytes")
            check_length(
                nonce, 8, "Invalid Nonce length. Nonce must be 8 bytes.")
            self.nonce = nonce

    def import_parameters(self, key=None, nonce=None):
        super().import_key(key)
        self.import_nonce(nonce)

    def make_cipher(self):
        # Validation
        check_none(self.key, "Key must be set")
        check_type(self.key, bytes, "Key must be bytes")
        check_length(self.key, AES_KEY_SIZE,
                     f"Invalid Key length. Key must be {AES_KEY_SIZE} bytes.")

        check_none(self.nonce, "Nonce must be set")
        check_type(self.nonce, bytes, "Nonce must be bytes")
        check_length(
            self.nonce, 8, "Invalid Nonce length. Nonce must be 8 bytes.")

        self.cipher = AES.new(self.key, AES.MODE_CTR, nonce=self.nonce)

    def encrypt(self, plain_text: bytes) -> bytes:
        self.make_cipher()
        cipher_text = self.cipher.encrypt(plain_text)
        return cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        self.make_cipher()
        plain_text = self.cipher.decrypt(cipher_text)
        return plain_text


"""Electronic codebook (ECB)
┌────────────────────────────┐ ┌────────────────────────────┐
│         ┌───────────┐      │ │          ┌───────────┐     │
│         │ Plaintext │      │ │          │Ciphertext │     │
│         └─────┬─────┘      │ │          └─────┬─────┘     │
│               │            │ │                │           │
│               ▼            │ │                ▼           │
│┌───┐    ┌───────────┐      │ │ ┌───┐    ┌───────────┐     │
││Key├───▶│ENCRYPTION │      │ │ │Key├───▶│DECRYPTION │     │
│└───┘    └─────┬─────┘      │ │ └───┘    └─────┬─────┘     │
│               │            │ │                │           │
│               ▼            │ │                ▼           │
│         ┌───────────┐      │ │          ┌───────────┐     │
│         │Ciphertext │      │ │          │ Plaintext │     │
│         └───────────┘      │ │          └───────────┘     │
└────────────────────────────┘ └────────────────────────────┘
"""


class AES_ECB(AES_Cryptography):
    def __init__(self):
        super().__init__()

    def generate_parameters(self):
        super().generate_key()

    def import_parameters(self, key=None, nonce=None):
        super().import_key(key)

    def make_cipher(self):
        # Validation
        check_none(self.key, "Key must be set")
        check_type(self.key, bytes, "Key must be bytes")
        check_length(self.key, AES_KEY_SIZE,
                     f"Invalid Key length. Key must be {AES_KEY_SIZE} bytes.")

        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, plain_text: bytes) -> bytes:
        self.make_cipher()
        cipher_text = self.cipher.encrypt(pad(plain_text, AES.block_size))
        return cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        self.make_cipher()
        plain_text = unpad(self.cipher.decrypt(cipher_text), AES.block_size)
        return plain_text


"""Cipher block chaining (CBC)
CBC is a widely used mode that provides confidentiality and is suitable for sequential encryption and decryption.
Each block of plaintext is XORed with the previous ciphertext block before encryption, adding randomness and diffusion.
CBC mode can be used for encrypting image files, but it may not be ideal for random access.
┌──────────────────────────────────────────────────────────────────────────────┐
│         ┌───────────┐             ┌───────────┐             ┌───────────┐    │
│         │ Plaintext │             │ Plaintext │             │ Plaintext │    │
│         └─────┬─────┘             └─────┬─────┘             └─────┬─────┘    │
│               │                         │                         │          │
│               ▼                         ▼                         ▼          │
│   ┌────┐     .─.                       .─.                       .─.         │
│   │ IV ├───▶( X )      ┌─────────────▶( X )      ┌─────────────▶( X )        │
│   └────┘     `┬'       │               `┬'       │               `┬'         │
│               │        │                │        │                │          │
│               ▼        │                ▼        │                ▼          │
│┌───┐    ┌───────────┐  │ ┌───┐    ┌───────────┐  │ ┌───┐    ┌───────────┐    │
││Key├───▶│ENCRYPTION ├──┘ │Key├───▶│ENCRYPTION ├──┘ │Key├───▶│ENCRYPTION │    │
│└───┘    └─────┬─────┘    └───┘    └─────┬─────┘    └───┘    └─────┬─────┘    │
│               │                         │                         │          │
│               ▼                         ▼                         ▼          │
│         ┌───────────┐             ┌───────────┐             ┌───────────┐    │
│         │Ciphertext │             │Ciphertext │             │Ciphertext │    │
│         └───────────┘             └───────────┘             └───────────┘    │
└──────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────┐
│         ┌───────────┐             ┌───────────┐             ┌───────────┐    │
│         │Ciphertext ├──┐          │Ciphertext ├──┐          │Ciphertext │    │
│         └─────┬─────┘  │          └─────┬─────┘  │          └─────┬─────┘    │
│               │        │                │        │                │          │
│               ▼        │                ▼        │                ▼          │
│┌───┐    ┌───────────┐  │ ┌───┐    ┌───────────┐  │ ┌───┐    ┌───────────┐    │
││Key├───▶│DECRYPTION │  │ │Key├───▶│DECRYPTION │  │ │Key├───▶│DECRYPTION │    │
│└───┘    └─────┬─────┘  │ └───┘    └─────┬─────┘  │ └───┘    └─────┬─────┘    │
│               │        │                │        │                │          │
│               ▼        │                ▼        │                ▼          │
│   ┌────┐     .─.       │               .─.       │               .─.         │
│   │ IV ├───▶( X )      └─────────────▶( X )      └─────────────▶( X )        │
│   └────┘     `┬'                       `┬'                       `┬'         │
│               │                         │                         │          │
│               ▼                         ▼                         ▼          │
│         ┌───────────┐             ┌───────────┐             ┌───────────┐    │
│         │ Plaintext │             │ Plaintext │             │ Plaintext │    │
│         └───────────┘             └───────────┘             └───────────┘    │
└──────────────────────────────────────────────────────────────────────────────┘
"""


class AES_CBC(AES_Cryptography):
    def __init__(self):
        super().__init__()
        self.iv = None

    def generate_iv(self):
        self.iv = get_random_bytes(16)

    def generate_parameters(self):
        super().generate_key()
        self.generate_iv()

    def import_iv(self, iv: bytes):
        # Validation
        if iv:
            check_type(iv, bytes, "Nonce must be bytes")
            check_length(
                iv, 16, "Invalid Nonce length. Nonce must be 16 bytes.")
            self.iv = iv

    def import_parameters(self, key=None, iv=None):
        super().import_key(key)
        self.import_iv(iv)

    def make_cipher(self):
        # Validation
        check_none(self.key, "Key must be set")
        check_type(self.key, bytes, "Key must be bytes")
        check_length(self.key, AES_KEY_SIZE,
                     f"Invalid Key length. Key must be {AES_KEY_SIZE} bytes.")

        check_none(self.iv, "IV must be set")
        check_type(self.iv, bytes, "IV must be bytes")
        check_length(self.iv, 16, "Invalid IV length. IV must be 16 bytes.")

        self.cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)

    def encrypt(self, plain_text: bytes) -> bytes:
        self.make_cipher()
        cipher_text = self.cipher.encrypt(pad(plain_text, AES.block_size))
        return cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        self.make_cipher()
        plain_text = unpad(self.cipher.decrypt(cipher_text), AES.block_size)
        return plain_text


"""
# Example useage
key16 = b'[\xd7\xa7\xb1\x94@\xb1\xa0\xb7\xee"\xc9\x10\xfc\x08\xfa'
key32 = b'J\x04<F>\x18\x84\x91\xd2\xe4yM\xb7A\xdc64\xadM\x15\x86/\xae\x0b\xdf\xc8jJ[?\xac~'
nonce8 = b'\xa0\x99\x9b\x13\x81\xb6\x1c\xb9'
iv16 = b'\xcabg\x91\x82\x028\xcbH\xaf\x92\xe2.\x85n+'

aes_cipher = AES_ECB()
# aes_cipher.generate_parameters()
aes_cipher.import_parameters(key=key32)

# aes_cipher = AES_CTR()
# aes_cipher.generate_parameters()
# aes_cipher.import_parameters(key=key32,nonce=nonce8)

# aes_cipher = AES_CBC()
# aes_cipher.generate_parameters()
# aes_cipher.import_parameters(key=key32, iv=iv16)


plain_text = b"hello"
cipher_text = aes_cipher.encrypt(plain_text)
print(cipher_text)

decrypted_text = aes_cipher.decrypt(cipher_text)
print(decrypted_text)

cipher_text = aes_cipher.encrypt(plain_text)
print(cipher_text)

decrypted_text = aes_cipher.decrypt(cipher_text)
print(decrypted_text)

cipher_text = aes_cipher.encrypt(plain_text)
print(cipher_text)

decrypted_text = aes_cipher.decrypt(cipher_text)
print(decrypted_text)
"""