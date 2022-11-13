from pprint import pprint


dict_ = [{"bin": bin(i), "dec": (i), "hex": hex(i), "oct": oct(i)} for i in range(16)]


pprint(dict_)
