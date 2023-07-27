def solution(sequence, k):
    n = len(sequence)
    ret = [0, n]
    curr, i, j = sequence[0], 0, 0
    
    while j < n-1:
        if curr == k and ret[1] - ret[0] > j - i:
            ret = [i, j]
            j += 1
            curr += sequence[j]
        elif curr < k:
            j += 1
            curr += sequence[j]
        else:
            curr -= sequence[i]
            i += 1
    
    while i < n:
        if curr == k and ret[1] - ret[0] > j - i:
            ret = [i, j]
        elif curr > k:
            curr -= sequence[i]
            i += 1
        else:
            break
        
    return ret