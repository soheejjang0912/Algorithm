def solution(numbers):
    answer = []    
    numbers.sort()
    
    result = set()
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:
                result.add(numbers[i] + numbers[j])

    
    return sorted(result)