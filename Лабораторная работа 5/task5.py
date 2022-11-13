import string
import random
def get_random_password(n: int = 8) -> str:
    chars = string.digits + string.ascii_letters
    return "".join(random.sample(chars, n))

print(get_random_password())