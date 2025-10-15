def solution(s):
    n = len(s)
    i = 0
    answer = 0

    while i < n:
        x = s[i]
        same = 0
        diff = 0
        j = i

        # 현재 구간을 읽어가며 same/diff 카운트
        while j < n:
            if s[j] == x:
                same += 1
            else:
                diff += 1
            j += 1

            # 같아지면 여기서 끊기
            if same == diff:
                break

        # 하나의 분리 완성 (j는 다음 구간의 시작 인덱스)
        answer += 1
        i = j  # 남은 부분부터 다시 시작

    return answer
