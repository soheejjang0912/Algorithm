def solution(wallpaper):
    rows, cols = len(wallpaper), len(wallpaper[0])
    
    min_row, min_col = rows, cols
    max_row, max_col = 0, 0
    
    for i in range(rows):
        for j in range(cols):
            if wallpaper[i][j] == "#":
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    
    return [min_row, min_col, max_row + 1, max_col + 1]
