from pprint import pprint
keys = ["dec", "bin", "oct", "hex"]
dict = [{"bin": bin(i), "dec": (i), "hex": hex(i), "oct": oct(i)} for i in range(16)]
pprint(dict)