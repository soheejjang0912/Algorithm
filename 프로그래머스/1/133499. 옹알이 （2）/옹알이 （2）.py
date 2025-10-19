def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    count = 0

    for b in babbling:
        i = 0
        prev = ""
        valid = True

        while i < len(b):
            matched = False
            for w in words:
                if b.startswith(w, i):  # 해당 위치에서 단어 일치?
                    if w == prev:        # 바로 직전 단어와 같으면 불가능
                        valid = False
                        break
                    prev = w
                    i += len(w)
                    matched = True
                    break
            if not matched:  # 어느 단어와도 일치하지 않으면 불가능
                valid = False
                break
        
        if valid:
            count += 1

    return count
