ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sanitize_input(text):
    return text.replace(" ", "").upper()

def validate_text(text):
    for char in text:
        if char not in ALPHABET:
            raise ValueError(f"Invalid character '{char}' in the text. Text must contain only Latin alphabet letters.")
    return text

def validate_key2(key2):
    if len(key2) < 7:
        raise ValueError("Key 2 must have a length of at least 7 characters.")
    for char in key2:
        if char not in ALPHABET:
            raise ValueError("Key 2 must contain only Latin alphabet letters.")
    return key2

def generate_shifted_alphabet(key2):
    unique_chars = ""
    for char in key2:
        if char not in unique_chars:
            unique_chars += char

    shifted = unique_chars
    for char in ALPHABET:
        if char not in unique_chars:
            shifted += char

    return shifted

def cezar_encrypt(text, key):
    source_alphabet = ALPHABET
    result = ""
    for char in text:
        idx = source_alphabet.index(char)
        result += source_alphabet[(idx + key) % 26]
    return result

def cezar_decrypt(text, key):
    source_alphabet = ALPHABET
    result = ""
    for char in text:
        idx = source_alphabet.index(char)
        result += source_alphabet[(idx - key) % 26]
    return result

def cezar_encrypt_2keys(text, key1, key2):
    encrypted_text = cezar_encrypt(text, key1)
    result = ""
    source_alphabet = ALPHABET
    key2_alphabet = generate_shifted_alphabet(key2)
    for char in encrypted_text:
        idx = source_alphabet.index(char)
        result += key2_alphabet[idx]
    return result

def cezar_decrypt_2keys(text, key1, key2):
    source_alphabet = ALPHABET
    key2_alphabet = generate_shifted_alphabet(key2)
    intermediate_text = ""
    for char in text:
        idx = key2_alphabet.index(char)
        intermediate_text += source_alphabet[idx]
    return cezar_decrypt(intermediate_text, key1)

def main():
    global ENCRYPTED_MESSAGE

    while True:
        print("Choose the operation:")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Encrypt with 2 keys")
        print("4 - Decrypt with 2 keys")
        print("0 - Exit")

        choice = input("Select option: ")

        if choice == '0':
            break

        if choice in ['1', '3']:
            message = input("Enter the message for encryption: ")
            sanitized_message = sanitize_input(message)

            try:
                validate_text(sanitized_message)
            except ValueError as e:
                print(e)
                continue

            key1 = int(input("Enter key 1 (between 1 and 25 inclusive): "))
            if not 1 <= key1 <= 25:
                print("Incorrect key 1. Enter a value between 1 and 25.")
                continue

            if choice == '1':
                ENCRYPTED_MESSAGE = cezar_encrypt(sanitized_message, key1)
                print("The encrypted message is:", ENCRYPTED_MESSAGE)
            else:
                key2 = input("Enter key 2 (minimum 7 characters): ")
                try:
                    key2 = validate_key2(sanitize_input(key2))
                except ValueError as e:
                    print(e)
                    continue

                ENCRYPTED_MESSAGE = cezar_encrypt_2keys(sanitized_message, key1, key2)
                print("Shifted alphabet based on key2:", generate_shifted_alphabet(key2))
                print("The encrypted message with 2 keys is:", ENCRYPTED_MESSAGE)

        elif choice in ['2', '4']:
            encrypted_message = input("Enter the encrypted message for decryption: ")
            sanitized_message = sanitize_input(encrypted_message)

            try:
                validate_text(sanitized_message)
            except ValueError as e:
                print(e)
                continue

            key1 = int(input("Enter key 1 (between 1 and 25 inclusive): "))
            if not 1 <= key1 <= 25:
                print("Incorrect key 1. Enter a value between 1 and 25.")
                continue

            if choice == '2':
                decrypted_message = cezar_decrypt(sanitized_message, key1)
                print("The decrypted message is:", decrypted_message)
            else:
                key2 = input("Enter key 2: ")
                try:
                    key2 = validate_key2(sanitize_input(key2))
                except ValueError as e:
                    print(e)
                    continue

                decrypted_message = cezar_decrypt_2keys(sanitized_message, key1, key2)
                print("The decrypted message with 2 keys is:", decrypted_message)

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    ENCRYPTED_MESSAGE = ""
    main()
