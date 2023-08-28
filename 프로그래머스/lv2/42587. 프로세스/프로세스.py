from collections import deque

def solution(priorities, location):
    
    result = []
    queue = deque()
    
    # basic
    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))
        
    while queue:		
        current = queue.popleft()
        
        if any(current[0] < idx[0] for idx in queue):
            queue.append(current)
            
        else:
            result.append(current)
            
            if current[1] == location:
                return len(result)

    for idx, priority in enumerate(result):
            if priority[1] == location:
                return idx + 1