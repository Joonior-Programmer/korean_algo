def solution(targets):
    ret = 0
    targets.sort(key=lambda x: x[1])
    
    end = 0
    
    for start, e in targets:
        if start >= end:
            ret += 1
            end = e
    return ret