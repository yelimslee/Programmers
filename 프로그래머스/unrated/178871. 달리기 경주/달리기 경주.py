def solution(players, callings):
    maps = {player: idx for idx, player in enumerate(players)}
    
    for player in callings:
        # 현재 호출된 유저의 순위(인덱스) curPlayer에 할당
        curPlayer = maps[player]
        # maps에 저장된 현재 호출된 유저 순위 -1
        maps[player] -= 1
        # maps에 저장된 호출된 유저의 앞에 있던 유저 순위 +1
        maps[players[curPlayer-1]] += 1
        # players list에 저장된 두 유저의 위치 교체
        players[curPlayer-1], players[curPlayer] = players[curPlayer], players[curPlayer-1]
        
        # 위 코드가 어렵다면, 아래처럼 작성해도 됨
        # temp = players[curPlayer]
        # players[curPlayer] = players[curPlayer - 1]
        # players[curPlayer - 1] = temp
            
    return players
