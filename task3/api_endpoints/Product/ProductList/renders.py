from cryptography.fernet import Fernet


def encrypt(cls, value):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(value.encode())
    return encrypted_text.decode(), key.decode()



def decrypt(cls, encrypted_text, key):
    cipher_suite = Fernet(key.encode())
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
    return decrypted_text.decode()


def serialize(price, marja, package_code):
    encrypted_price, price_key = encrypt(str(price))
    encrypted_marja, marja_key = encrypt(str(marja))
    encrypted_package_code, package_code_key = encrypt(package_code)

    return {
        'price': encrypted_price,
        'marja': encrypted_marja,
        'package_code': encrypted_package_code,
        'keys': {
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