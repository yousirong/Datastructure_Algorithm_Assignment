#                1.제목:한국외대 자료구조 과제(괄호 검사)
#                2.날짜:20210404
def solution(s):
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for c in s:   # input으로 문자열을 받아서 한 문자씩 루프
        if c in '({[':     # 한 문자가 열린괄호 일경우
            stack.append(c)   # 스택 리스트에 append
        elif c in ')}]':      # 한 문자가 닫힌괄호 일경우
            if stack:
                top = stack.pop()  # top 변수에 스택에 저장되어있는 제일 위의 문자 pop
                if d[c] != top:    # d 변수의 set에서 괄호의 짝이 아닐 경우
                    return False   # False 반환
            else:
                return False       # 위의 모든 경우 아닐 경우 반환
    return len(stack) == 0         # 스택을 비움

p = input()
if(solution(p) == False):      # solution 함수에서 반환한 값이 False 일 경우
    print("0")                # 0출력
else:
    print("1")               # 반환 값이 True 일 경우 1출력
