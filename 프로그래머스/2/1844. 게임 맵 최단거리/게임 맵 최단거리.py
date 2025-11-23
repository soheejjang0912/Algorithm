from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # map check
    map_check = [[False]*m for _ in range(n)]
    map_check[0][0] = True 
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
     
    q = deque()
    q.append((0, 0, 1))
     
    while q:
        x, y, dist = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and map_check[nx][ny] == False and maps[nx][ny] == 1 :
                map_check[nx][ny] = True
                q.append((nx, ny, dist+1))
    
    return -1