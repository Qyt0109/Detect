from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

from SecurityScheme.Cryptography.rsa_based import RSABased
from SecurityScheme.Cryptography.CommonHelper.validation import check_none, check_type


class DSS_RSA_PSS(RSABased):

    def sign(self, message: bytes) -> bytes:
        """
        Create a PSS signer with the private key and sign the message
        """
        check_type(message, bytes, "Message must be bytes")
        self.CheckKey(self.private_key)

        message_hash = SHA256.new(message)

        try:
            signer = DSS_RSA_PSS.CreateSignerOrVerifier(self.private_key)
            signature = signer.sign(message_hash)
            return signature
        except ValueError as e:
            raise ValueError("Error occurred while signing the message") from e

    def verify(self, message: bytes, signature: bytes) -> bool:
        """
        Create a PSS verifier with the public key and verify the message with the signature
        """
        check_type(message, bytes, "Message must be bytes")
        check_type(signature, bytes, "Signature must be bytes")
        self.CheckKey(self.public_key)

        message_hash = SHA256.new(message)

        try:
            verifier = DSS_RSA_PSS.CreateSignerOrVerifier(
                self.public_key)
            verifier.verify(message_hash, signature)
            return True
        except (ValueError, TypeError):
            return False
        except Exception as e:
            raise ValueError(
                "Error occurred while verifying the signature") from e

    @staticmethod
    def CreateSignerOrVerifier(key: bytes):
        check_type(key, bytes, "Key must be in bytes")
        try:
            RSA_public_key = RSA.import_key(key)
            signer_or_verifier = pss.new(RSA_public_key)
            return signer_or_verifier
        except (ValueError, TypeError):
            raise ValueError(
                "Error occurred while creating signer or verifier")


"""# Example useage
private_key = RSABased.KeyFromPath("/media/psf/AllFiles/Applications/CODESTUFF/DoAnCode/AppMayBanTocDo/SecurityScheme/Cryptography/A_private_4096.pem")
public_key = RSABased.KeyFromPath("/media/psf/AllFiles/Applications/CODESTUFF/DoAnCode/AppMayBanTocDo/SecurityScheme/Cryptography/A_public_4096.pem")


# Create an instance of RsaPssSignature
rsa_pss = RSA_PSS_Signature()

#rsa_pss.generate_key_pair()
rsa_pss.import_key_pair(private_key=private_key, public_key=public_key)

# Define the message to be signed
message = b'This is the message to be signed'

# Sign the message using the private key
signature = rsa_pss.sign(message)

# Verify the signature using the public key
is_valid = rsa_pss.verify(message, signature)

if is_valid:
    print("The signature is valid.")
else:
    print("The signature is not valid.")


    

"""
