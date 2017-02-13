import random
import string

def random_string(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(random_string())
print(random_string(size=50))
