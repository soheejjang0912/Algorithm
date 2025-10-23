import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        # 외부 원 내부의 최대 y
        max_y = int(math.floor((r2**2 - x**2) ** 0.5))
        # 내부 원 내부의 최소 y
        min_y = int(math.ceil((r1**2 - x**2) ** 0.5)) if x < r1 else 0
        answer += max_y - min_y + 1  # (y는 0부터 max_y까지)
    return answer * 4