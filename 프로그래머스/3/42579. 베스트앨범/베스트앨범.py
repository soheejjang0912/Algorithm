def solution(genres, plays):
    answer = []
    
    # 가장 높은 genres -> 해시 dict
    genre_sum = {}
    genre_song = {} 

    for i in range(len(genres)):   # index가 필요함
        g = genres[i]
        p = plays[i]

        if g not in genre_sum:
            genre_sum[g] = 0
            genre_song[g] = []     # 리스트로 초기화

        genre_sum[g] += p
        genre_song[g].append((i, p))   # i = 고유 번호
    
    sorted_genre = sorted(genre_sum.items(), key=lambda x: x[1], reverse=True)
      
     
 
    for g, _ in sorted_genre: 
        genre_song[g].sort(key=lambda x: (-x[1], x[0]))
        
        for i, _ in genre_song[g][:2]:

            answer.append(i)
     
     
    return answer