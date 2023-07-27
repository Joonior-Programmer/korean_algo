def solution(sequence, k):
    n = len(sequence)
    ret = [0, n]
    curr, i, j = sequence[0], 0, 0
    
    while j < n:
        if curr == k and ret[1] - ret[0] > j - i:
            ret = [i, j]
            curr -= sequence[i]
            i += 1
        elif curr < k:
            if j + 1 == n:
                break
            j += 1
            curr += sequence[j]
        else:
            curr -= sequence[i]
            i += 1
        
    return ret