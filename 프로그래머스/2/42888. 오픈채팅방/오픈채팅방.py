 

def solution(record):
    answer = [] 
    
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