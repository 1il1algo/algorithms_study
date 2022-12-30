#14502 로봇 청소기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
count = 0
r, c, d = map(int, input().split())
Map = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    Map[i] = list(map(int, input().split()))

def mov(r, c, d):
    if d == 0:
        return r-1, c, d
    elif d == 1:
        return r, c+1, d
    elif d == 2:
        return r+1, c, d
    elif d == 3:
        return r, c-1, d

def clean(r, c, d):
    global count
    if (Map[r][c] == 0):
        Map[r][c] = 2
        count += 1
    
    for i in range(4):
        #왼쪽으로 회전
        d = (d+3)%4
        nr, nc, nd = mov(r, c, d)
        #왼쪽으로 회전한 후 앞에 청소할 공간이 있는지 확인
        if Map[nr][nc] == 0:
            clean(nr, nc, nd)
            return
    #네 방향 모두 청소가 이미 되어있거나 벽인 경우
    nr, nc, nd = mov(r, c, (d + 2)%4)
    if Map[nr][nc] == 1:
        return
    else:
        clean(nr, nc, d)
        return
clean(r, c, d)
print(count)