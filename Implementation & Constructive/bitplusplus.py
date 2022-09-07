import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def bitplusplus ():
    n, res = int(input().decode()), 0
    for i in range(n):
        line = input().decode()
        for ch in line:
            if (ch == '+'):
                res += 1 ; break
            if (ch == '-'):
                res -= 1 ; break
    sys.stdout.write(str(res) + '\n')
 
bitplusplus()
