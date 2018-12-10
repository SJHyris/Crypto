from binascii import hexlify

plaintext = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = b"ICE"
def repeat_encrypt(plaintext, key):
    cyphtxt = b''
    i = 0
    while i < len(plaintext):
        k = i%len(key)
        value = plaintext[i] ^ key[k]
        cyphtxt += bytes([value])
        i += 1
    crypto = str(hexlify(cyphtxt))
    print(crypto)

repeat_encrypt(plaintext, key)


