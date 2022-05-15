import random
random.seed(302266)
print(''.join(chr(random.randrange(256) ^ c)
    for c in bytes.fromhex('876095D97C6D7DD62EB754D1E4BFE74DD63A8C1FC2')
    if random.randrange(2)))

print(''.join(chr(random.randrange(256) ^ c)
    for c in bytes.fromhex('876095D97C6D7DD62EB754D1E4BFE74DD63A8C1FC2')
    if random.randrange(2)))
