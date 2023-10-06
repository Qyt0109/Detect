from SecurityScheme.template_security_scheme import TemplateSecurityScheme, TemplateSecurityModel

from SecurityScheme.Cryptography.pkc_rsa import PKC_RSA_OAEP
from SecurityScheme.Cryptography.dss_rsa import DSS_RSA_PSS
from SecurityScheme.Cryptography.skc_aes import AES_CBC, AES_CTR, AES_ECB


class SecurityModel(TemplateSecurityModel):

    def init_pkc(self):
        rsa_pkc = PKC_RSA_OAEP()
        return rsa_pkc

    def init_skc(self):
        aes_skc = AES_CBC()
        return aes_skc

    def init_dss(self):
        rsa_dss = DSS_RSA_PSS
        return rsa_dss


class SecurityScheme(TemplateSecurityScheme):
    def init_security_model(self) -> None:
        security_model = SecurityModel()
        return security_model