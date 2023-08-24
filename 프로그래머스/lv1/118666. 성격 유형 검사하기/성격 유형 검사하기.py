def solution(survey, choices):
    score_map = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }
    
    scores = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    for i, q in enumerate(survey):
        score = score_map.get(choices[i])
        if choices[i] <= 3:
            scores[q[0]] += score
        else:
            scores[q[1]] += score
      
    result = ""
    result += 'R' if scores['R'] >= scores['T'] else 'T'
    result += 'C' if scores['C'] >= scores['F'] else 'F'
    result += 'J' if scores['J'] >= scores['M'] else 'M'
    result += 'A' if scores['A'] >= scores['N'] else 'N'
    
    return result
