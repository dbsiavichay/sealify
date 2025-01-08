from src.core.app.exceptions import BaseException


class InvalidCertificateException(BaseException):
    message = "El certificado no es válido"
    status_code = 400

    def __init__(self):
        super().__init__(self.message, self.status_code)


class UnprocessableCertificateException(BaseException):
    message = "No se pudo procesar el certificado"
    status_code = 422

    def __init__(self):
        super().__init__(self.message, self.status_code)


class CertificateInvalidKeysException(BaseException):
    message = "El archivo de firma no contiene claves válidas"
    status_code = 400

    def __init__(self):
        super().__init__(self.message, self.status_code)
