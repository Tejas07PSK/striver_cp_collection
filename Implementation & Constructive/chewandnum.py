import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def chewandnum ():
    n_str = input().decode().splitlines()[0]
    res, i = ['' for ch in n_str], 0
    for ch in n_str:
        num = int(ch)
        if (5 <= num < 9): num = 9 - num
        if ((num == 9) or (num == 0)):
            if ((i > 0) and (res[i - 1] != '')): res[i] = '0'
            else: res[i] = '9' if (num == 9) else ''
        else: res[i] = str(num)
        i += 1
    res = ''.join(res)
    sys.stdout.write((res if (res != '') else '0'))
 
chewandnum()
