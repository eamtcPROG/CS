import hashlib
import math
from random import randint

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2


# Function to generate keys
def gen_keys(p, g):
    k_pr = randint(1, p - 1)
    e = pow(g, k_pr, p)
    k_pub = (p, g, e)  # Public key
    return {"pub_key": k_pub, "pr_key": k_pr}


# Function to get signature
def get_signature(p, g, k_pr, message):
    k_E = 0
    while True:
        x = randint(1, p - 1)
        if math.gcd(x, p - 1) == 1:
            k_E = x
            break

    r = pow(g, k_E, p)
    k_E_inv = pow(k_E, -1, p - 1)
    hash_object = hashlib.sha256(message.encode())
    hex_dig = hash_object.hexdigest()
    S = (k_E_inv * (int(hex_dig, 16) - k_pr * r)) % (p - 1)

    return (r, S)


# Function to verify signature
def verify_signature(p, g, e, signature, message):
    r, S = signature
    if not (1 <= r and r <= p - 1):
        return False
    hashed_message = (pow(e, r, p) * pow(r, S, p)) % p
    hash_object = hashlib.sha256(message.encode())
    hex_dig = hash_object.hexdigest()
    decrypted_hash = pow(g, int(hex_dig, 16), p)

    print("hashed_message: ", hashed_message)
    print("decrypted_hash: ",decrypted_hash)

    return hashed_message == decrypted_hash

message = "In summary, one of the most notable vulnerabilities inherent in monogbetic ciphers lies in their susceptibility to frequency analysis attacks. Within any given language, there are specific frequencies with which certain letters appear; for instance, in the English language, the letters ’e’ and ’t’ occur with high frequency. With a sufficiently large ciphertext sample, it is possible to discern patterns that align with the known letter frequencies of the language used in the original message. Such discernable patterns provide cryptanalysts the opportunity to make educated inferences regarding the substitution techniques utilized, thereby facilitating the decryption process. While monogbetic ciphers were historically deemed secure, the advent of frequency analysis techniques has significantly undermined their efficacy, particularly when a large corpus of ciphertext is available for analysis. Consequently, the utility of these ciphers has been relegated primarily to educational contexts and as puzzles, rather than as robust mechanisms for ensuring the confidentiality of communications. As cryptographic methodologies have evolved, so too have the means for securing communications. Contemporary cryptographic algorithms are markedly more intricate and are engineered to resist a multiplicity of attack vectors. Nonetheless, the examination of the strengths and weaknesses inherent in foundational ciphers like the monogbetic variants provides invaluable insights into the principles that have shaped the trajectory of cryptographic security."

keys = gen_keys(p, g)
print("Public key: ", keys['pub_key'])
print("Private key: ", keys['pr_key'])

signature = get_signature(p, g, keys['pr_key'], message)
print("Signature: ", signature)

is_valid = verify_signature(p, g, keys['pub_key'][2], signature, message)
print("Signature valid: ", is_valid)
