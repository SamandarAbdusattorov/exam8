from cryptography.fernet import Fernet
from django.http import JsonResponse

# AES encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_data(request):
    data = request.GET.get('data', '')
    encrypted_data = cipher_suite.encrypt(data.encode())
    return JsonResponse({'encrypted_data': encrypted_data.decode()})


def decrypt_data(request):
    encrypted_data = request.GET.get('encrypted_data', '')
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return JsonResponse({'decrypted_data': decrypted_data.decode()})
