def solution(phone_book):
    # phone_book을 순회하면서 전체 전화번호를 키로 가지는 딕셔너리 생성
    table = {}
        
        #value는 True로 설정
    for num in phone_book:
        table[num] = True
    
    # phone_book을 다시 순회하며, 각각의 전화번호를 가지고 
    for number in phone_book:
        str = ""
        # 문자열을 맨 앞부터 잘라서 더해가며, 해당 문자열을 키로 가지는 값이 테이블에 있다면
        for char in number[:-1]:
        # for idx in range(0, lenn(number) -1) 과 같음
        
            str += char
            if str in table:
            # 접두어가 존재하는 것으로, False를 반환
                return False
        
    # 순회가 모두 종료될 때까지 False를 반환하지 않는다면, 접두어가 없으므로 True 반환
    answer = True
    return True