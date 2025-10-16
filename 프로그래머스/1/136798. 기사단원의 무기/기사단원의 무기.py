def solution(number, limit, power):
    def count_divisors(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:  # 제곱수 중복 방지
                    count += 1
        return count

    total = 0
    for i in range(1, number + 1):
        attack = count_divisors(i)
        if attack > limit:
            attack = power
        total += attack

    return total
