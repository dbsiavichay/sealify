from src.core.app.exceptions import BaseException


class CertificateInvalidExtensionException(BaseException):
    message = "El certificado debe ser: .p12"
    status_code = 400

    def __init__(self, detail: str = None):
        super().__init__(self.status_code, self.message, detail)


class InvalidPasswordOrCertificateException(BaseException):
    message = "Contraseña incorrecta o certificado inválido"
    status_code = 400

    def __init__(self, detail: str = None):
        super().__init__(self.status_code, self.message, detail)


class UnprocessableCertificateException(BaseException):
    message = "No se pudo procesar el certificado"
    status_code = 422

    def __init__(self, detail: str = None):
        super().__init__(self.status_code, self.message, detail)


class CertificateInvalidKeysException(BaseException):
    message = "El archivo de firma no contiene claves válidas"
    status_code = 400

    def __init__(self, detail: str = None):
        super().__init__(self.status_code, self.message, detail)
