from itertools import product

from itertools import product

def solution(word):
    dic = ['A', 'E', 'I', 'O', 'U']
    words = []

    # 모든 조합 생성
    for length in range (1, 6):
        for p in product(dic, repeat=length): 
            words.append(''.join(p))
             
    words.sort()  
    return words.index(word) + 1
