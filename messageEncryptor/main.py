from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    key = generate_key()
    message = input("\nEnter a message to Encrypt : ")

    encrypted_message = encrypt_message(key, message)
    print(f"\nEncrypted Message : {encrypted_message}")

    print("\nKey used : ", key)

    decrypted_message = decrypt_message(key, encrypted_message)
    print(f"\nDecrypted Message : {decrypted_message}")
    print("\n")