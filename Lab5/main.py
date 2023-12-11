from sympy import randprime
import random
# p and q prime
# n = p*q
#f(n) = (p-1)(q-1)
#e => 1<e<f(n) e prime f(n) and n gdc(n)=1
#c=m^e mod n
#P(e,n)
#d*e mod f(n)=1
#Private(d,n)
#m = c^d mod n
# Function to generate a random prime number
def generate_prime_number(n_bits):
    min_value = 2 ** (n_bits - 1)
    max_value = 2 ** n_bits - 1
    return randprime(min_value, max_value)



# Extended GCD and Modular exponentiation functions
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular exponentiation
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Step 1: Generate two prime numbers p and q
p = generate_prime_number(1024)
q = generate_prime_number(1024)

# Step 2: Calculate n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose an encryption exponent e
e = 65537

# Step 4: Compute the decryption exponent d
_, d, _ = extended_gcd(e, phi)
d = d % phi



# Encrypt a message
message = "Coretchi Mihai"
decimal_message = int.from_bytes(message.encode(), 'big')
encrypted_message = mod_exp(decimal_message, e, n)

# Decrypt the message
decrypted_message = mod_exp(encrypted_message, d, n)
decrypted_text = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big').decode()

# Output the results
print("D",decimal_message)
print("Encrypted Message: ", encrypted_message)
print("Decrypted Text: ", decrypted_message)
print("Decrypted Text: ", decrypted_text)
