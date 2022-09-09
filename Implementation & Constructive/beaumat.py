import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def beaumat ():
    mat = [list(map(int, input().decode().splitlines()[0].split(' '))) for i in range(5)]
    mid_row, mid_col = 2, 2
    one_row, one_col = None, None
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == 1):
                one_row, one_col = i, j
                break
    sys.stdout.write(str(abs(mid_row - one_row) + abs(mid_col - one_col)) + '\n')
 
beaumat()
