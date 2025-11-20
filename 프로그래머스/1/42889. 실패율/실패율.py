def solution(N, stages):
    answer = []
    total = len(stages)        # 전체 플레이어 수
    
    # 1. 각 스테이지별 실패율 구하기
    for stage in range(1, N+1):
        in_stage = stages.count(stage)   # 현재 스테이지에서 멈춘 사람
        
        # 도달한 유저가 없는 경우 실패율은 0
        if total == 0:
            fail_per = 0
        else:
            fail_per = in_stage / total
        
        # 실패율 저장
        answer.append((stage, fail_per))
        
        # 3. 다음 스테이지의 '도달한 유저수' 계산
        total -= in_stage
     
    # 실패율 내림차순 / 스테이지 번호 오름차순 정렬
    answer.sort(key=lambda x: (-x[1], x[0]))
    
    # 스테이지만 반환
    return [stage for stage, rate in answer]
   
    