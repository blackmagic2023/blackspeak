from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad_message(message):
    block_size = 16
    num_bytes_to_pad = block_size - len(message) % block_size
    padded_message = message + num_bytes_to_pad * chr(num_bytes_to_pad)
    return padded_message

def unpad_message(padded_message):
    num_bytes_to_remove = ord(padded_message[-1])
    return padded_message[:-num_bytes_to_remove]

def encrypt_message(message, key):
    padded_message = pad_message(message)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded_message.encode())
    return base64.b64encode(ciphertext)

def decrypt_message(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(encrypted_message)
    padded_message = cipher.decrypt(ciphertext).decode()
    return unpad_message(padded_message)

def main():
    key = get_random_bytes(16)  # Generate a random 128-bit (16-byte) key
    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print("Encrypted message:", encrypted_message.decode())

        elif choice == '2':
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(encrypted_message.encode(), key)
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
