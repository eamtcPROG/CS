import random

# Function for modular exponentiation
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# ElGamal Encryption Function
def encrypt(message, p, g, y):
    k = random.randint(1, p - 2)
    c1 = mod_exp(g, k, p)
    c2 = (message * mod_exp(y, k, p)) % p
    return c1, c2

# ElGamal Decryption Function
def decrypt(c1, c2, p, x):
    return (c2 * mod_exp(c1, p - 1 - x, p)) % p

# Define Parameters and Keys
p = int("32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039")
g = 2

# Private key
x = random.randint(1, p - 2)

# Public key
y = mod_exp(g, x, p)

# Convert "Coretchi Mihai" to Decimal
message = "Coretchi Mihai"
decimal_message = [ord(char) for char in message]

# Encrypt Each Character in the Message
encrypted_message = [encrypt(m, p, g, y) for m in decimal_message]

# Decrypt Each Character in the Encrypted Message
decrypted_message = [decrypt(c1, c2, p, x) for c1, c2 in encrypted_message]

# Output
print("Coretchi Mihai in Decimal Form: ", decimal_message)
print("Decrypted Message in Decimal Form: ", decrypted_message)
print("Encrypted Message: ", encrypted_message)
