# n: 참가자 수 
# a: 참가자 번호
# b: 경쟁자 번호
 
def solution(n,a,b):
    answer = 0  
    while a != b: 
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
         
    return answer