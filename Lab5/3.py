import random
#p - primie
#g = primitive root
# a and b in [1,p-1]
#Pk = A=g^a mod p
#B=g^b mod p
#S A = B^a mod p
#S B = A^b mod p
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

# Define Parameters
p = int("32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039")
g = 2

# Generate secret numbers for Alice (a) and Bob (b)
a = random.randint(1, p - 1)
b = random.randint(1, p - 1)

# Compute public keys
A = mod_exp(g, a, p)
B = mod_exp(g, b, p)

# Compute the common keys
common_key_alice = mod_exp(B, a, p)
common_key_bob = mod_exp(A, b, p)

# Output the results
print("Alice's Common Key:", common_key_alice)
print("Bob's Common Key:", common_key_bob)
print("Keys are identical:", common_key_alice == common_key_bob)
