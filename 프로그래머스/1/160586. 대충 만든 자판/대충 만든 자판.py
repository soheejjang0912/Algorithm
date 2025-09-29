def solution(keymap, targets):
    # 1. 각 문자별 최소 키 입력 횟수 계산
    min_press = {}
    for key in keymap:
        for idx, char in enumerate(key):
            # idx는 0부터 시작 → 눌러야 하는 횟수는 idx+1
            if char in min_press:
                min_press[char] = min(min_press[char], idx + 1)
            else:
                min_press[char] = idx + 1

    # 2. targets 계산
    result = []
    for word in targets:
        total = 0
        for char in word:
            if char not in min_press:  # 만들 수 없는 경우
                total = -1
                break
            total += min_press[char]
        result.append(total)

    return result
