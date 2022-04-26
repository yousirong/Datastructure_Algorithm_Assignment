#                1.제목:한국외대 자료구조 과제(괄호 검사)
#                2.날짜:20210405
def solution(s):   # 괄호 검사 함수
    d = {          # d 라는 변수에 짝이 맞는 괄호 set으로 만듦
        ')': '(',
        '}': '{',
        ']': '[',
        '{': '}',
        '(': ')',
        '[': ']'
    }
    stack = []    # stack변수
    count = 0     # 오류난 곳 인데스 반환 변수
    for c in s:   # 한 문자씩 for 루프
        if c in '({[':  # 한 문자가 열린 괄호 일 경우
            count += 1  # 한 문자를 검사 했으므로 count +1
            stack.append(c)  # 열린 괄호는 스택에 append
        elif c in ')}]':    # 한 문자가 닫힌 괄호 일 경우
            if stack:
                top = stack.pop()  # top 변수에 스택에서 맨위의 원소 pop
                if d[c] != top:    # 괄호가 짝이 아닐 경우
                    errnum = count  # 오류 난 인덱스 반환 변수 errnum
                    err.append(d[c])  # 전역 변수 err 리스트에 대응하는 괄호가 없는 괄호는 append
                    return False, errnum   # 에러일 경우 False와 에러 인덱스 반환
            else:
                errnum = count   # 닫힌괄호가 아닌 대응하는 열린 괄호가 없는 경우
                err.append(d[c])  # 전역 변수 err에 닫힌 괄호가 없는 괄호를 append
                return False, errnum  # 에러일 경우 False와 에러 인덱스 반환
        elif c == ' ':    # 문자가 빈칸일 경우 자리수 +1
            count += 1
            continue      # 빈칸은 오류 아님 자리인데스 + 1
        else:
            count += 1    # 괄호가 아닌 다른 숫자나 문자가 올경우 그냥 자리 인덱스 +1
    if (len(stack)!=0):   # 스택에 값이 남아 있을경우 ( 오류 검출 )
        top = stack.pop()   # top변수에 처음으로 발견된(짝을 찾지 못한 괄호) pop
        count = len(s)     # count변수에 입력받은 문자열 길이
        s = ''.join(reversed(s))    # 입력받은 문자열을 뒤집음
        for c in s:        # 뒤집힌 문자열에서 처음부터 검사해서 처음으로 발견된 자리 인덱스
            count -= 1     # 검출하는 알고리즘
            if c in top:
                errnum = count
                err.append(d[c])      # 오류난 괄호의 짝을 err리스트에 append
                return False, errnum   # 오류 검출 했으므로 False와 오류난 자리 인덱스 반환
            elif c == ' ':
                count += 1
                continue

    return True, 1, len(stack) == 0   # 오류 검출 함수에서 정상적으로 입력 받았을 경우 True 반환

err = []   # 짝을 찾지 못한 경우 그 괋호에 대응 하는 괄호 반환 변수
count = 0   # 오류 자리 인덱스 반환 변수
p = input()
x = solution(p)
if str(solution(p)[0]) == "False":  # 짝이 맞지 않는 경우
    if err[:-1] == ['(']:     # [:-1] 인것은 처음으로 발견된 ( 짝을 찾지 못한 경우) 오류
        print(x[1], "error1")  # 를 반환 하기 위함
    elif err[:-1] == ['{']:
        print(x[1], "error2")
    elif err[:-1] == ['[']:
        print(x[1], "error3")
    elif err[:-1] == [')']:
        print(x[1], "error4")
    elif err[:-1] == ['}']:
        print(x[1], "error5")
    elif err[:-1] == [']']:
        print(x[1], "error6")
else:
    print("1")  # 짝이 맞는 경우 1출력
