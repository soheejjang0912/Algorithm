# 
# 

def solution(record):
    answer = []
    
    # 해시?로 아이디 닉네임 저장
    # Change 작업 완료
    
    # Change제외한 record 이용하여 resulst 생성
    
    nickname = {}
    
    for i in range(len(record)):
        record_split = record[i].split() 
        
        if record_split[0] == "Enter" or record_split[0] == "Change":
            nickname[record_split[1]] = record_split[2]
    
    for i in record: 
        record_split = i.split() 
        
        action = record_split[0] 
        id = record_split[1] 
        
        if action == "Enter":
            answer.append(nickname[id] + "님이 들어왔습니다.")
        
        elif action == "Leave":
             answer.append(nickname[id] + "님이 나갔습니다.") 
        
    return answer