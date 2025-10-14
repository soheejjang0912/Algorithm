def solution(s):
    last_index = {}  # 각 문자의 마지막 등장 위치 저장
    result = []

    for i, ch in enumerate(s):
        if ch in last_index:
            result.append(i - last_index[ch])  # 이전 등장 위치와의 거리
        else:
            result.append(-1)  # 처음 등장한 문자
        last_index[ch] = i  # 현재 위치로 갱신

    return result
