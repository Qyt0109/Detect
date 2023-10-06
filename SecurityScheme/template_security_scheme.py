from SecurityScheme.Cryptography.pkc_rsa import RSA_Cryptography, RSA
from SecurityScheme.Cryptography.CommonHelper.device_operator import get_mac_address, mac_address_to_str, validate_mac_address
from SecurityScheme.Cryptography.skc_aes import AES_Cryptography, AES_ECB, AES_CBC, AES_CTR
from SecurityScheme.Cryptography.dss_rsa import DSS_RSA_PSS
from abc import abstractmethod
import requests
from http import HTTPStatus
import os

from pydantic import BaseModel
import base64


class BinaryData(BaseModel):
    data: str


server_root = "https://9225-113-22-85-225.ngrok-free.app"
server_handshake = "/handshake/start"
server_public_key_url = "/server-resources/public-key"


class TemplateSecurityModel():
    def __init__(self) -> None:
        self.my_pkc = self.init_pkc()
        self.other_pkc = self.init_pkc()
        self.dss = self.init_dss()
        self.skc = self.init_skc()

    @abstractmethod
    def init_pkc(self) -> RSA_Cryptography:
        pass

    @abstractmethod
    def init_skc(self) -> AES_Cryptography:
        pass

    @abstractmethod
    def init_dss(self) -> DSS_RSA_PSS:
        pass


class TemplateSecurityScheme():
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """

    def __init__(self) -> None:
        self.security_model = self.init_security_model()

    # These operations have to be implemented in subclasses.
    @abstractmethod
    def init_security_model(self) -> TemplateSecurityModel:
        pass

    """SYMMETRIC KEY EXCHANGE WITH CONFIDENTIALITY, AUTHENTICATION AND NON-REPUDIATION

        PUb PUa PRa                                     PUa PUb PRb
        ┌───────────┐                                   ┌───────────┐
        │Client - a │                                   │Server - b │
        └───────────┘                                   └───────────┘
                │                                               │
                │    E(PUb, Na || IDa)                          │
        Na      │───────────────────────┐                       │
                │        STEP 1         └──────────────────────▶│   Na  IDa
                │                                               │
                │                           E(PUa, Na || Nb)    │
                │                       ┌───────────────────────│   Nb
    Na == Na ?  │◀──────────────────────┘        STEP 2         │
    => Nb       │                                               │
                │       E(PUb, Nb)                              │
                │───────────────────────┐                       │
                │        STEP 3         └──────────────────────▶│   Nb == Nb ?
                │                                               │   =>
                │   E(PUb, E(PRa, Key))                         │
                │───────────────────────┐                       │
                │        STEP 4         └──────────────────────▶│   Key
                │                                               │
    """

    def hand_shake(self):
        PUb = self.GetServerPublicKey()                                     # PUb
        self.security_model.other_pkc.import_key_pair(public_key=PUb)
        self.security_model.my_pkc.generate_key_pair()
        PRa, PUa = self.security_model.my_pkc.export_key_pair()             # PRa   PUa
        # IDa
        IDa = get_mac_address()
        IDa_str = mac_address_to_str(IDa)

        # Client hello
        print("Start client hello")
        print(PUa.decode())
        print(IDa_str)
        hello_msg = PUa.decode() + IDa_str
        response = requests.post(
            server_root + server_handshake, json=BinaryData(data=hello_msg).dict())
        print(response.status_code)
        if response.status_code == HTTPStatus.OK:
            print("PUa sended")
        else:
            print("Failed:", response.status_code)
        # Step 1
        # Na
        Na = os.urandom(4)

        step_1_msg = self.security_model.other_pkc.encrypt(
            Na+IDa)          # E(PUb, Na || IDa)

    @staticmethod
    def GetServerPublicKey() -> bytes:
        server_respond = requests.get(server_root + server_public_key_url)
        if server_respond.status_code == 200:
            data = server_respond.json()
            public_key = data.get("public-key").encode()
            rsa_key = RSA.import_key(public_key).export_key()
            return rsa_key
        else:
            print("Failed to retrieve the server's public key")
