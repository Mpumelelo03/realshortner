import string
def encode_base62(num: int) -> str:
    chars = string.digits + string.ascii_letters
    base = 62
    s = []
    while num > 0:
        s.append(chars[num % base])
        num //= base
    return ''.join(reversed(s)) or '0'

print(encode_base62(12345)) 

