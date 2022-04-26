#                1.제목:한국외대 자료구조 과제(후위 수식 계산)
#                2.날짜:20210407
class Stack:
    def __init__(self):  # 스택 생성자 초기화
        self.items = []

    def push(self, j):   # push 함수를 쓸경우 스택에 해당인자 push
        self.items.append(j)

    def pop(self):     # pop에서 스택이 비어 있을 경우 indexError예외 처리하고 error 반환
        try:
            return self.items.pop()
        except IndexError:
            print('error1')

def evaluation(expr):   # expr : list   expr은 공백을 제외한 원소들로만 구성되어있음
    s = Stack()
    op = '+-*//%'  # op = ('+','-','*','//', '%')
    for item in expr:  # 리스트의 원소를 하나씩 검사
        if item in op:  # 원소가 연사자일 경우 pop 두번해서 연산하고 다시 push 하는 과정
            right_opr = s.pop()   # 첫번째 원소 pop  두 번째 원소 pop
            left_opr = s.pop()  # operand: 피연산자, operator: 연산자
            if item == '+':
                s.push(left_opr + right_opr)
            elif item == '-':
                s.push(left_opr - right_opr)
            elif item == '*':
                s.push(left_opr * right_opr)
            elif item == '//':
                s.push(left_opr // right_opr)
            elif item == '%':
                s.push(left_opr % right_opr)
        elif item == ';':   # 원소가 세미콜론일 경우 for구문 break
            break
        else:
            s.push(int(item))    # 원소가 연산자가 아닐 경우는 이문제에서는 정수 와 상수뿐이므로 push
    if len(s.items) > 1:    # 스택에 원소가 남아 있을 경우
        return 'error2'    # 오류임
    else:
        return s.pop()    # 오류가 아닐경우 후위수식 결과값 pop해서 반환


def switch(exprStr):    # 사용자의 입력을 공백으로 spilt해서 받아온 리스트를 정수 따로 연산자따로 변환해서 리스트화 하는 함수
    x = []
    op = '+', '*', '%', '-', ';'  # - 연산자는 - 정수부분 처리를 위해 따로 처리
    oi = '0123456789'        # // 연산자도 문자길이가 2이므로 따로 처리
    val = ''    # //와 - 연산자를 제외한 자머지 연사자를 처리하기 위한 변수
    val1 = ''   # // 연사자를 처리하기 위한 변수
    for c in exprStr:     # 리스트의 원소 한개씩 검사
        if len(c) == 1:   # 원소가 길이 한개 인 것들은 append함
            x.append(c)
        elif c[0] in '-':  # -(피연산자) 0보다 작은 정수의 경우는 스트링 [0]검사해서 '-'있으면 append
            x.append(c)
        elif len(c) > 1:  # 피연산자와 연산자가 붙어 있는 경우 떼어내는 부분
            for s in c:  # 한 글자씩 검사
                if s in op:   # 한글자가 연산자일 경우
                    x.append(val)  # val변수는 연산자 이전에 숫자가 있을 경우 val에 저장하여
                    val = ''       # 연산자를 만날경우 숫자 반환하고 다시 초기화
                    x.append(s)    # 새로운 리스트 x에 append 하는 부분
                elif s in oi:    # oi는 숫자임
                    val += s     # 숫자일 경우 val 변수에 string으로 이어 붙이기
                elif s == '/':    # // 연산자도 길이가 2이므로 문자 한개씩 검사하 하다가 //만날경우
                    val1 += '/'   # 숫자 string 이어 붙이기와 같은 메커니즘으로 //가 될경우 append
                    if val1 == '//':
                        x.append(val1)   # 새로운 리스트 x에 append합니다.
            x.append(val)   # 그냥 길이가 1이상인 숫자만 있을 경우 val에 저장된 숫자 append
            val = ''
    while '' in x:
        x.remove('')  # x리스트 안에 ['']원소는 모두 삭제
    return x


def main():
    expr = input().split()
    result = switch(expr)
    try:
        print(evaluation(result))
    except:  # 모든 예외는 그냥 '' 출력하게 함.
        print('')

if __name__ == '__main__':
    main()


