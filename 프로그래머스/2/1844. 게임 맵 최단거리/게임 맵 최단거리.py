from collections import deque

def solution(maps):
    n = len(maps) # 행 개수
    m = len(maps[0]) # 열 개수
    
    # 방문 여부 저장
    visited = [[False]*m for _ in range(n)]
    
    # bfs
    q = deque()
    q.append((0, 0, 1)) # 행, 열, 거리
    visited[0][0] = True
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, dist = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))
        
        
    return -1