from django.db import models
from django.db.models import CharField, DecimalField
from cryptography.fernet import Fernet


class Product(models.Model):
    title = CharField(max_length=123)
    price = DecimalField(max_digits=10, decimal_places=2)
    marja = DecimalField(max_digits=10, decimal_places=2)
    package_code = CharField(max_length=10)

    def __str__(self):
        return self.title

    @classmethod
    def encrypt(cls, value):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(value.encode())
        return encrypted_text.decode(), key.decode()

    @classmethod
    def decrypt(cls, encrypted_text, key):
        cipher_suite = Fernet(key.encode())
        decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
        return decrypted_text.decode()

    def serialize(self):

        encrypted_price, price_key = self.encrypt(str(self.price))
        encrypted_title, title_key = self.encrypt(str(self.title))
        encrypted_marja, marja_key = self.encrypt(str(self.marja))
        encrypted_package_code, package_code_key = self.encrypt(self.package_code)

        return {
            'price': encrypted_price,
            'title': encrypted_title,
            'marja': encrypted_marja,
            'package_code': encrypted_package_code,
            'keys': {
                'title': title_key,
                'price': price_key,
                'marja': marja_key,
                'package_code': package_code_key
            }
        }

    @classmethod
    def deserialize(cls, data):
        decrypted_price = cls.decrypt(data['price'], data['keys']['price'])
        decrypted_marja = cls.decrypt(data['marja'], data['keys']['marja'])
        decrypted_package_code = cls.decrypt(data['package_code'], data['keys']['package_code'])

        return {
            'price': decrypted_price,
            'marja': decrypted_marja,
            'package_code': decrypted_package_code
        }
