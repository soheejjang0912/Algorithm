def solution(players, callings):
    # 선수 이름 → 등수
    player_to_rank = {player: i for i, player in enumerate(players)}
    # 등수 → 선수 이름
    rank_to_player = {i: player for i, player in enumerate(players)}
    
    for name in callings:
        cur_rank = player_to_rank[name]       # 현재 등수
        front_rank = cur_rank - 1             # 바로 앞 등수 선수
        
        # 앞 선수
        front_player = rank_to_player[front_rank]
        
        # swap 처리
        player_to_rank[name] = front_rank
        player_to_rank[front_player] = cur_rank
        
        rank_to_player[cur_rank] = front_player
        rank_to_player[front_rank] = name
    
    # 등수 순으로 선수 이름 반환
    return [rank_to_player[i] for i in range(len(players))]
