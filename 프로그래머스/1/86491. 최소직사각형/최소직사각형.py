# [큰값, 작은값] 으로 정렬

# 해당 배열의 작은값 중 가장 작은값과 큰값 구하기

# 해당 값 곱하기

def solution(sizes):
    answer = 0
    
    sort_array = []
    for i, j in sizes :
        if i > j :
            sort_array.append([i,j])
        else :
            sort_array.append([j,i])
      
    max_w = max(w for w, h in sort_array)
    max_h =  max(h for w, h in sort_array)
    return max_w * max_h