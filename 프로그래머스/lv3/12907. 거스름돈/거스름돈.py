def solution(n, money):
    table = [[0 for _ in range(n + 1)] for _ in range(len(money) + 1)]
    
    table[0][0] = 1
    
    for i in range(1, len(money) + 1):
        before_init(table, i, money[i-1])
        curMoney = money[i - 1]
        for j in range(curMoney, n + 1):
            table[i][j] = (table[i - 1][j] + table[i][j - curMoney]) % 1000000007
    
    answer = table[-1][-1]
    return answer

def before_init(table, i, num):
    for idx in range(num):
        table[i][idx] = table[i - 1][idx]