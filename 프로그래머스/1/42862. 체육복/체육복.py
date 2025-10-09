def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 빌려줄 수 있는 경우 처리
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    # 전체 학생 수에서 체육복을 못 빌린 학생 수 빼기
    return n - len(lost_set)