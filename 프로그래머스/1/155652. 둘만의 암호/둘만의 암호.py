def solution(s, skip, index):
    from string import ascii_lowercase
    
    alphabet = list(ascii_lowercase)
    available = [ch for ch in alphabet if ch not in skip]
    
    result = ''
    for ch in s:
        i = available.index(ch)
        result += available[(i + index) % len(available)]
    
    return result
