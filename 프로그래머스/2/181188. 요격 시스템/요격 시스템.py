def solution(targets):
    # 끝점을 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    count = 0
    current = -1  # 마지막 요격 미사일 x좌표
    
    # 순회하면서 필요한 최소 요격 미사일 계산
    for s, e in targets:
        # 현재 요격 좌표가 이 구간을 커버하지 못하면 새로 쏨
        if s >= current:
            count += 1
            current = e  # 새 요격 미사일을 e 직전에 둔다 (e 자체는 포함 안 됨)
    
    return count
