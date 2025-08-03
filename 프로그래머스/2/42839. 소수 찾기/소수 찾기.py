# numbers의 값 하나씩 문자열로 변경 후 
# 모든 경우의 수 만들기

# 소수 판별하기

from itertools import permutations

def solution(numbers):
    
    numbers_list = list(numbers)
    print(numbers_list)

    result_set = set()

    for i in range(1, len(numbers_list)+1):
        print(i)
        
        for p in permutations(numbers_list, i):
            num = int("".join(p)) # "" : 붙일 때 아무 것도 사이에 넣지 말고 붙여라!
            result_set.add(num)

    
        prime_count = 0

        for num in result_set:
            if is_prime(num):
                prime_count +=1

    return prime_count

def is_prime(n):
    if n < 2:
        return False;
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True