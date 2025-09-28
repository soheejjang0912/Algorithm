def solution(n, m, section):
    count = 0
    i = 0
    while i < len(section):
        start = section[i]
        end = start + m - 1
        count += 1
        # 이번 칠로 커버되는 구역을 건너뛴다
        while i < len(section) and section[i] <= end:
            i += 1
    return count
