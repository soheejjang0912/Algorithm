def solution(X, Y):
    # 0~9 숫자 등장 횟수 세기
    count_X = [0] * 10
    count_Y = [0] * 10
    
    for x in X:
        count_X[int(x)] += 1
    for y in Y:
        count_Y[int(y)] += 1
    
    # 공통으로 등장하는 숫자 수만큼 결과 리스트에 추가
    result = []
    for i in range(9, -1, -1):  # 큰 수부터
        common = min(count_X[i], count_Y[i])
        result.extend([str(i)] * common)
    
    if not result:
        return "-1"  # 공통 숫자 없음
    if result[0] == '0':
        return "0"   # 공통 숫자가 0으로만 구성
    return ''.join(result)
