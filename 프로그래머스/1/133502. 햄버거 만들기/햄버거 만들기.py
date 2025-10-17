def solution(ingredient):
    stack = []
    count = 0
    
    for i in ingredient:
        stack.append(i)
        # 마지막 4개가 [1,2,3,1]인지 확인
        if stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 포장 → 재료 제거
            count += 1
            del stack[-4:]
    
    return count
