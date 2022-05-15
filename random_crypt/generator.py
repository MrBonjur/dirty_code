import random
from random import Random

text = 'test message'
time_seed = random.randint(0, 999999)


def generate_bytes_for_seed(seed: int, message: str) -> bytearray:
    data = Random(seed)
    garbage = Random(34988394)

    data.seed(seed)
    result = bytearray()
    i = 0
    while i < len(message):
        c = message[i]
        if data.randrange(2):
            result.append(data.randrange(256) ^ ord(c))
            i += 1
        else:
            result.append(garbage.randrange(256))
    return result


code = f"""import random
random.seed({time_seed})
print(''.join(chr(random.randrange(256) ^ c)
    for c in bytes.fromhex({repr(generate_bytes_for_seed(time_seed, text).hex().upper())})
    if random.randrange(2)))
"""

file = open("example.py", "w")
file.write(code)
file.close()
print(code)
