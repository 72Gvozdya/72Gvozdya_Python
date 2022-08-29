def subgen(x):
    for i in range(x):
        yield i

def gen(y):
    yield from subgen(y)

for q in gen(6):
    print(q)

