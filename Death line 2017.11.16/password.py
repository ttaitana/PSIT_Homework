"""password"""
import hashlib as hb
import codecs as cd
def encode(code):
    """encode function"""
    print(code)
encode(hb.sha512(cd.encode(input())).hexdigest().upper())

