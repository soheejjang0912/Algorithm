def solution(park, routes):
    H, W = len(park), len(park[0])
    
    # 시작 지점 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                r, c = i, j
    
    # 방향 정의
    directions = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        dr, dc = directions[op]
        
        nr, nc = r, c
        valid = True
        
        # 이동 시뮬레이션
        for _ in range(n):
            nr += dr
            nc += dc
            if not (0 <= nr < H and 0 <= nc < W):  # 범위 초과
                valid = False
                break
            if park[nr][nc] == "X":  # 장애물
                valid = False
                break
        
        # 이동 가능할 때만 반영
        if valid:
            r, c = nr, nc
    
    return [r, c]
