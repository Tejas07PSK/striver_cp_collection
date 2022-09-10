import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def softdrinking ():
    n, k, l, c, d, p, nl, np = map(int, input().decode().splitlines()[0].split(' '))
    res = min((k * l // nl), (c * d), (p // np)) // n
    sys.stdout.write(str(res) + '\n')

softdrinking()
