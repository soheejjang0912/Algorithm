def solution(s):  
    answer = 0;
    
    for i in range(len(s)):
        check_s = s[i:] + s[:i]
        if is_valid(check_s):
            answer += 1
    return answer 

def is_valid(s):
    stack = []
    pair = {')':'(', ']': '[', '}':'{'}
    
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return len(stack) == 0
    
        
        
    
        
        
        
        