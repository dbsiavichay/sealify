from cryptography.fernet import Fernet


class CipherUtil:
    def __init__(self, cipher: Fernet):
        self.cipher = cipher

    def encrypt(self, plain_text: str) -> str:
        encrypted_text = self.cipher.encrypt(plain_text.encode("utf-8"))
        return encrypted_text.decode("utf-8")

    def decrypt(self, encrypted_text: str) -> str:
        plain_text = self.cipher.decrypt(encrypted_text).decode("utf-8")
        return plain_text
