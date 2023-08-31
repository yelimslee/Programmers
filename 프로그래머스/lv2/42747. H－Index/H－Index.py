def solution(citations):
    citations.sort(reverse = True)
    result = 0
    
    for i in range(len(citations)):
        if i + 1<= citations[i]:
            result = i + 1
            
        else:
            break

    return result