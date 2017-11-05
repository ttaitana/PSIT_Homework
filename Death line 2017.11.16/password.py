"""password"""
import hashlib as hb
import codecs as cd
print(hb.sha512(cd.encode(input())).hexdigest().upper())
