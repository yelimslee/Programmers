def solution(today, terms, privacies):
    # 결과를 저장할 리스트를 초기화
    answer = []

    # 입력받은 "today" 날짜를 년, 월, 일로 분리하여 정수로 변환
    today_year, today_month, today_day = map(int, today.split('.'))
    
    # 주어진 날짜 "today"로부터 일수로 변환
    todayData = today_day + (today_month * 28) + (today_year * 12 * 28)

    # 약관 기간을 저장할 딕셔너리를 초기화
    maps = {}

    # 입력받은 "terms" 리스트를 순회하며 각 약관의 기간을 저장
    for term in terms:
        key, value = term.split()
        # 약관에 따른 일수 변환하여 딕셔너리에 저장
        maps[key] = int(value) * 28

    # 입력받은 "privacies" 리스트를 순회
    for idx, privacie in enumerate(privacies):
        # 날짜와 약관 종류를 분리합니다.
        date_str, termKey = privacie.split()
        # 날짜를 년, 월, 일로 분리하여 정수로 변환
        year, month, day = map(int, date_str.split('.'))
        # 약관에 따른 일수를 가져옴
        termValue = maps.get(termKey)

        # 약관 기간이 존재하는 경우
        if termValue is not None:
            # 날짜를 일수로 변환하고, 약관 기간을 더하여 총 일수를 계산
            termData = day + (month * 28) + (year * 12 * 28) + termValue - 1
            
            # 총 일수가 오늘의 일수보다 작다면, 파기하지 않아도 되는 약관
            if termData < todayData:
                answer.append(idx + 1)

    # 결과 리스트를 반환
    return answer
