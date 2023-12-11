from sympy import randprime
import hashlib

def generate_prime_number(n_bits):
    min_value = 2 ** (n_bits - 1)
    max_value = 2 ** n_bits - 1
    return randprime(min_value, max_value)

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# RSA key generation
p = generate_prime_number(1536)
q = generate_prime_number(1536)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537  # Public exponent
_, d, _ = extended_gcd(e, phi)
d = d % phi  # Private exponent

# Hash function for signing
def hash_message(message):
    return int.from_bytes(hashlib.sha384(message.encode()).digest(), byteorder='big')

# Sign a message
def sign_message(message, d, n):
    hashed_message = hash_message(message)
    signature = mod_exp(hashed_message, d, n)
    return signature

# Verify a signature
def verify_signature(message, signature, e, n):
    hashed_message = hash_message(message)
    print("hashed_message",hashed_message)
    decrypted_hash = mod_exp(signature, e, n)
    print("decrypted_hash", decrypted_hash)
    return hashed_message == decrypted_hash

# Example usage
message = "In summary, one of the most notable vulnerabilities inherent in monoalphabetic ciphers lies in their susceptibility to frequency analysis attacks. Within any given language, there are specific frequencies with which certain letters appear; for instance, in the English language, the letters ’e’ and ’t’ occur with high frequency. With a sufficiently large ciphertext sample, it is possible to discern patterns that align with the known letter frequencies of the language used in the original message. Such discernable patterns provide cryptanalysts the opportunity to make educated inferences regarding the substitution techniques utilized, thereby facilitating the decryption process. While monoalphabetic ciphers were historically deemed secure, the advent of frequency analysis techniques has significantly undermined their efficacy, particularly when a large corpus of ciphertext is available for analysis. Consequently, the utility of these ciphers has been relegated primarily to educational contexts and as puzzles, rather than as robust mechanisms for ensuring the confidentiality of communications. As cryptographic methodologies have evolved, so too have the means for securing communications. Contemporary cryptographic algorithms are markedly more intricate and are engineered to resist a multiplicity of attack vectors. Nonetheless, the examination of the strengths and weaknesses inherent in foundational ciphers like the monoalphabetic variants provides invaluable insights into the principles that have shaped the trajectory of cryptographic security."
# Replace with your actual message
signature = sign_message(message, d, n)
is_valid = verify_signature(message, signature, e, n)

print("Signature:", signature)
print("Signature valid:", is_valid)


