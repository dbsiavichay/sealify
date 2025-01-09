import base64
import logging
import os
import subprocess
from tempfile import NamedTemporaryFile
from uuid import uuid4

import jks
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509 import load_der_x509_certificate
from cryptography.x509.oid import NameOID

from src.certificate.app.exceptions import (
    CertificateInvalidKeysException,
    InvalidPasswordOrCertificateException,
    UnprocessableCertificateException,
)
from src.certificate.domain.models import Certificate
from src.config import config
from src.core.domain.usecases import UseCase

logger = logging.getLogger(__name__)


class ProcessCertificateFileUseCase(UseCase):
    def execute(self, cert_bytes: bytes, password: str) -> Certificate:
        try:
            pkcs12.load_pkcs12(cert_bytes, password.encode())
        except ValueError as e:
            raise InvalidPasswordOrCertificateException(str(e))

        p12_file = NamedTemporaryFile(suffix=".p12")

        with open(p12_file.name, "wb") as file:
            file.write(cert_bytes)

        try:
            keystore_name = f"{uuid4()}.jks"
            command = config.KEYTOOL_COMMAND.format(
                p12_file.name, keystore_name, password, password
            )
            output = subprocess.check_output(
                command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
            )
            logger.info("PROCESS_CERTIFICATE_FILE :: SUCCESS :: %s", output)
        except subprocess.CalledProcessError as e:
            raise UnprocessableCertificateException(
                "COMMAND {0} :: RETURN_CODE {1} :: OUTPUT {2}".format(
                    command, e.returncode, e.output
                )
            )

        ks = jks.KeyStore.load(keystore_name, password)
        keys = [k for k in ks.private_keys.values() if "signing key" in k.alias]
        os.remove(keystore_name)

        if not keys:
            raise CertificateInvalidKeysException()

        key = keys.pop()

        if not key.is_decrypted():
            key.decrypt(password)

        cert_digest = key.cert_chain[0][1]
        cert = base64.b64encode(cert_digest).decode()
        key = base64.b64encode(key.pkey).decode()
        cert_x509 = load_der_x509_certificate(cert_digest)
        subject = cert_x509.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        certificate = Certificate(
            **{
                "id": uuid4(),
                "subject_name": subject[0].value,
                "serial_number": str(cert_x509.serial_number),
                "issue_date": cert_x509.not_valid_before_utc,
                "expiry_date": cert_x509.not_valid_after_utc,
                "cert": cert,
                "key": key,
            }
        )

        return certificate
