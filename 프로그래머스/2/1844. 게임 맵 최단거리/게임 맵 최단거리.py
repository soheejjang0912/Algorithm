
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
def solution(maps):
    stack = [(0,0, 1)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while stack:
        x, y, d= stack.pop(0)
        for q in range(4):
            ny = y + dy[q]
            nx = x + dx[q]
            if ny <0 or nx <0 or ny >= len(maps) or nx >= len(maps[0]):
                continue
            else:
                if maps[ny][nx] ==1 or maps[ny][nx] > d+1:
                    maps[ny][nx] =d+1 
                    if ny == len(maps) -1 and nx == len(maps[0])-1:
                        return d+1
                    stack.append((nx, ny, d+1))
    return -1