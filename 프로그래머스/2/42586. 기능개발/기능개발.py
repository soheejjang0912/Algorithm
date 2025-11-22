import math

def solution(progresses, speeds):
    
    answer = []
    # 1. 완성되는 일자 구하기
    days_left = [ math.ceil((100 - prog) / speed) for prog, speed in zip(progresses, speeds)]
    
    # 2. 완성된 일자 크기 구해서 묶기
    # [0] 숫자보다 큰 숫자 나올 때 까지 answer.append
    
    current = days_left[0]
    count = 1
    for i in range(1, len(days_left)):
        if days_left[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days_left[i]
            count = 1
    
    answer.append(count)
    
    return answer