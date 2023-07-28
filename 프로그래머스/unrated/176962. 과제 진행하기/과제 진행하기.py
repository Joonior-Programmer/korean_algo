def solution(plans):
    ret = []
    
    n = len(plans)
    
    for i in range(n):
        temp = plans[i][1].split(":")
        plans[i][1] = int(temp[0]) * 60 + int(temp[1])
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key=lambda x: x[1])
    stack = [plans[0]]
    
    print(plans)
    
    for i in range(1, n):
        time = plans[i][1] - plans[i-1][1]
    
        while stack and time:
            print(time, plans[i][0])
            if stack[-1][2] - time <= 0:
                time -= stack[-1][2]
                ret.append(stack.pop()[0])
            else:
                stack[-1][2] -= time
                time = 0
            
        stack.append(plans[i])
            
        
    
    while stack:
        ret.append(stack.pop()[0])
         
    return ret