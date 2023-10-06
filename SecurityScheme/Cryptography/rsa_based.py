"""PUBLIC KEY CRYPTOGRAPHY (PKC)
                        8888888b.    888     888   888888b.     888        8888888    .d8888b.          888    d8P    8888888888   Y88b   d88P                         
                        888   Y88b   888     888   888  "88b    888          888     d88P  Y88b         888   d8P     888           Y88b d88P                          
                        888    888   888     888   888  .88P    888          888     888    888         888  d8P      888            Y88o88P                           
                        888   d88P   888     888   8888888K.    888          888     888                888d88K       8888888         Y888P                            
                        8888888P"    888     888   888  "Y88b   888          888     888                8888888b      888              888                             
                        888          888     888   888    888   888          888     888    888         888  Y88b     888              888                             
                        888          Y88b. .d88P   888   d88P   888          888     Y88b  d88P         888   Y88b    888              888                             
                        888           "Y88888P"    8888888P"    88888888   8888888    "Y8888P"          888    Y88b   8888888888       888                             
                                                                                                                                                                       
                                                                                                                                                                       
                                                                                                                                                                       
     .d8888b.    8888888b.    Y88b   d88P   8888888b.    88888888888    .d88888b.     .d8888b.    8888888b.           d8888   8888888b.    888    888   Y88b   d88P    
    d88P  Y88b   888   Y88b    Y88b d88P    888   Y88b       888       d88P" "Y88b   d88P  Y88b   888   Y88b         d88888   888   Y88b   888    888    Y88b d88P     
    888    888   888    888     Y88o88P     888    888       888       888     888   888    888   888    888        d88P888   888    888   888    888     Y88o88P      
    888          888   d88P      Y888P      888   d88P       888       888     888   888          888   d88P       d88P 888   888   d88P   8888888888      Y888P       
    888          8888888P"        888       8888888P"        888       888     888   888  88888   8888888P"       d88P  888   8888888P"    888    888       888        
    888    888   888 T88b         888       888              888       888     888   888    888   888 T88b       d88P   888   888          888    888       888        
    Y88b  d88P   888  T88b        888       888              888       Y88b. .d88P   Y88b  d88P   888  T88b     d8888888888   888          888    888       888        
     "Y8888P"    888   T88b       888       888              888        "Y88888P"     "Y8888P88   888   T88b   d88P     888   888          888    888       888        
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from typing import Tuple

from SecurityScheme.Cryptography.CommonHelper.validation import check_length, check_none, check_type

# RSA

RSA_KEY_SIZE = 4096


class RSABased:
    """RSABased is a template class for RSA-based."""

    def __init__(self):
        self.private_key = None
        """RSA Private Key: The private key is used for decrypting ciphertext and signing data."""
        self.public_key = None
        """RSA Public Key: The public key is used for encrypting plaintext and verifying signatures."""

    def generate_key_pair(self, key_size=RSA_KEY_SIZE) -> None:
        """Generate a new RSA key pair with the specified key size."""
        self.private_key, self.public_key = self.GenerateKeyPair(key_size)

    def import_key_pair(self, private_key: bytes = None, public_key: bytes = None) -> None:
        """Import pre-existing private and public keys into the RSA_Cryptography instance."""
        # Validation
        if private_key is not None:
            self.CheckKey(private_key)
            self.private_key = private_key

        if public_key is not None:
            self.CheckKey(public_key)
            self.public_key = public_key

    def export_key_pair(self) -> Tuple[bytes, bytes]:
        """Export the private key and public key."""
        """Export the private key and public key."""
        if self.private_key is None or self.public_key is None:
            raise ValueError("No key pair available. Generate or import it first.")
        return self.private_key, self.public_key
    
    @staticmethod
    def CheckKey(key: bytes):
        check_none(key, "Key must be set")
        check_type(key, bytes, "Key must be bytes")
        try:
            RSA.import_key(key)  # Validate key
        except ValueError as e:
            raise ValueError("Invalid key format.") from e
    
    @staticmethod
    def GenerateKeyPair(key_size=RSA_KEY_SIZE) -> Tuple[bytes, bytes]:
        """Generate a new RSA key pair with the specified key size."""
        # Generate a new RSA key pair
        key_pair = RSA.generate(key_size)
        # Extract the private key and public key from the key pair
        private_key = key_pair.export_key()
        public_key = key_pair.publickey().export_key()
        return private_key, public_key
    
    @staticmethod
    def KeyFromPath(path:str)->bytes:
        try:
            # A get the key pair from the file
            with open(path, 'rb') as file:
                key = RSA.import_key(file.read()).export_key()
            return key
        except IOError as e:
            # Error handling
            print("Error occurred while loading key pair:", str(e))

