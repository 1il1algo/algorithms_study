import sys
input = sys.stdin.readline

n = int(input()) # 행렬의 크기
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))
    
color_list = [0, 0, 0] # color 개수 저장하는 곳

def paperSlice(y, x, n):
    color = paper[y][x]
    
    if n == 1: # 크기가 1이면 color 추가하고 종료
        color_list[color+1] += 1
        return 
    
    flag = 0
    for i in range(y, y+n): # 하나의 종이에서 다른 color가 있는지 확인
        for j in range(x, x+n):
            if paper[i][j] != color:
                flag = 1
                break
        if flag == 1:
            break
    
    l = n//3
        
    if flag == 0: # 모든 color가 같으면 color 추가하고 종료
        color_list[color+1] += 1
        return
    else: # 9번 재귀
        paperSlice(y, x, l)
        paperSlice(y, x+l, l)
        paperSlice(y, x+2*l, l)
        paperSlice(y+l, x, l)
        paperSlice(y+l, x+l, l)
        paperSlice(y+l, x+l*2, l)
        paperSlice(y+l*2, x, l)
        paperSlice(y+l*2, x+l, l)
        paperSlice(y+l*2, x+l*2, l)

paperSlice(0, 0, n)

for i in range(3):
    print(color_list[i])
        