from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from SecurityScheme.Cryptography.CommonHelper.validation import check_length, check_none, check_type
from SecurityScheme.Cryptography.rsa_based import RSABased


class RSA_Cryptography(RSABased):
    """RSA_Cryptography is a template class for RSA cryptography."""

    def encrypt(self, plaintext: bytes) -> bytes:
        """Encrypt the plaintext using the public key."""
        raise NotImplementedError(
            "Encrypt method must be implemented in subclass.")

    def decrypt(self, ciphertext: bytes) -> bytes:
        """Decrypt the ciphertext using the private key."""
        raise NotImplementedError(
            "Decrypt method must be implemented in subclass.")

# RSA with Optimal Asymmetric Encryption Padding (OAEP) scheme


class PKC_RSA_OAEP(RSA_Cryptography):
    """RSA_PKC_OAEP extends RSA_Cryptography and uses RSA encryption/decryption with Optimal Asymmetric Encryption Padding (OAEP) scheme."""

    def encrypt(self, plaintext: bytes) -> bytes:
        """Encrypt the plaintext using the public key."""
        # Validation
        check_type(plaintext, bytes, "Plaintext must be bytes")
        check_none(self.public_key,
                   "No public key available. Generate or import it first")

        try:
            # Create a cipher object with the public key
            cipher = PKCS1_OAEP.new(RSA.import_key(self.public_key))

            # Encrypt the plaintext
            ciphertext = cipher.encrypt(plaintext)

            return ciphertext
        except Exception as e:
            raise ValueError("Encryption failed.") from e

    def decrypt(self, ciphertext: bytes) -> bytes:
        """Decrypt the ciphertext using the private key."""
        # Validation
        # Validation
        check_type(ciphertext, bytes, "Ciphertext must be bytes")
        check_none(self.private_key,
                   "No private key available. Generate or import it first")

        try:
            # Create a cipher object with the private key
            cipher = PKCS1_OAEP.new(RSA.import_key(self.private_key))

            # Decrypt the ciphertext
            plaintext = cipher.decrypt(ciphertext)

            return plaintext
        except Exception as e:
            raise ValueError("Decryption failed.") from e


"""Example useage
pkc_rsa = RSA_PKC_OAEP()

private_key = RSABased.KeyFromPath(
    "/media/psf/AllFiles/Applications/CODESTUFF/DoAnCode/AppMayBanTocDo/SecurityScheme/Cryptography/A_private_4096.pem")
public_key = RSABased.KeyFromPath(
    "/media/psf/AllFiles/Applications/CODESTUFF/DoAnCode/AppMayBanTocDo/SecurityScheme/Cryptography/A_public_4096.pem")

pkc_rsa.import_key_pair(private_key, public_key)

message = b'Hello'
ciphertext = pkc_rsa.encrypt(message)
print(ciphertext.hex())
plaintext = pkc_rsa.decrypt(ciphertext)
print(plaintext)


"""
