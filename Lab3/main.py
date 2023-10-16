import re

def clean_input(input_str):
    return re.sub(r'[^a-zA-ZĂÂÎȘȚ]', '', input_str).upper()

def validate_key(key):
    if len(key) < 7:
        return False, "Key length must be at least 7."
    return True, ""


def create_matrix(key):
    alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i + 6] for i in range(0, 36, 6)]


def find_position(matrix, char):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == char:
                return i, j


def cipher_pair(matrix, a, b, encrypt=True):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        if encrypt:
            col_a, col_b = (col_a + 1) % 6, (col_b + 1) % 6
        else:
            col_a, col_b = (col_a - 1) % 6, (col_b - 1) % 6
    elif col_a == col_b:
        if encrypt:
            row_a, row_b = (row_a + 1) % 6, (row_b + 1) % 6
        else:
            row_a, row_b = (row_a - 1) % 6, (row_b - 1) % 6
    else:
        col_a, col_b = col_b, col_a

    return matrix[row_a][col_a] + matrix[row_b][col_b]


def playfair_cipher(matrix, text, encrypt=True):
    result = []
    i = 0

    if len(text) % 2 != 0:
        text += 'X'

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            b = 'X'

        result.append(cipher_pair(matrix, a, b, encrypt))
        i += 2

    return ''.join(result)



if __name__ == "__main__":
    while True:
        operation = input("Choose operation: encrypt | decrypt | exit: ").strip().lower()

        if operation == 'exit':
            break

        text = clean_input(input("Enter the text: "))
        key = clean_input(input("Enter the key: "))

        is_valid, message = validate_key(key)

        if not is_valid:
            print(message)
            continue

        matrix = create_matrix(key)

        if operation == 'encrypt':
            print("Encrypted text:", playfair_cipher(matrix, text))
        elif operation == 'decrypt':
            print("Decrypted text:", playfair_cipher(matrix, text, encrypt=False))
        else:
            print("Invalid operation.")
