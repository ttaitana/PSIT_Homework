"""password"""
import hashlib as hb
import codecs as cd
def decoding(coded):
    """decoding found"""
    _ = [print("%05d" %i) for i in range(100000) \
    if hb.sha512(cd.encode("%05d" %i)).hexdigest().upper() == coded]
decoding(input())
