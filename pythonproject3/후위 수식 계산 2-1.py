#                1.제목:한국외대 자료구조 과제(후위 수식 계산)
#                2.날짜:20210406
class Stack:
    def __init__(self):    # 스택 생성자 초기화
        self.items = []

    def push(self, j):    # push 함수를 쓸경우 스택에 해당인자 push
        self.items.append(j)

    def pop(self):     # pop에서 스택이 비어 있을 경우 indexError예외 처리하고 error 반환
        try:
            return self.items.pop()
        except IndexError:
            print('error')

def evaluation(expr):  # expr : list   expr은 공백을 제외한 원소들로만 구성되어있음
    s = Stack()
    op = '+-*//%'  # op = ('+','-','*','/')
    for item in expr:   # 리스트의 원소를 하나씩 검사
        if item in op:  # 원소가 연사자일 경우 pop 두번해서 연산하고 다시 push 하는 과정
            right_opr = s.pop()  # 첫번째 원소 pop  두 번째 원소 pop
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
            s.push(int(item))   # 원소가 연산자가 아닐 경우는 이문제에서는 정수 와 상수뿐이므로 push
    if len(s.items) > 1:   # 스택에 원소가 남아 있을 경우
        return 'error'   # 오류임
    else:
        return s.pop()   # 오류가 아닐경우 후위수식 계산한 값 pop해서 반환

def main():
    expr = input().split()  # expr: ['20','30','-','15','*',';']  문자열로 되어 있음
    try:
        print(evaluation(expr))
    except TypeError:    # 타입 에러일 경우 pop한 피 연산자들의 타입이 int형이 아닐 경우
        print('')        # 오류 except

if __name__ == '__main__':
    main()
