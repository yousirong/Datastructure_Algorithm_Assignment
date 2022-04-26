import string
# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789

class Stack:
    def __init__(self):   # 스택 생성자 초기화 및 set함수에 사용할 딕셔너리 변수 생성
        self.items = []
        self.value = 0
        self.dicitems = dict()   # 클래스에서 딕셔너리 생성자 만들때 self.변수이름 = dict()

    def push(self, e):     # push 함수를 쓸경우 스택에 해당인자 push
        self.items.append(e)

    def pop(self):     # pop에서 스택이 비어 있을 경우 indexError예외 처리하고 error1 반환
        try:
            return self.items.pop()
        except:
            print('error1')

    def eval(self, command):           # eval 명령어 양식: “eval 수식 ;”
        oi = string.ascii_letters  # 영어 대소문자 다 저장함
        x = []
        for item in command:   # command에는 eval 빼고 후위 수식만 들어 있음
            if item in oi:    # 영어 대소문자를 만날 경우는 변수로 인식함
                if item in self.dicitems:    # 그 변수가 딕셔너리 키에 있을 경우
                    x.append(str(self.dicitems[item]))   # 키에 해당하는 value값 x리스트 에 append
                else:
                    print("Error:", item, "is not defined")  # 키(변수)를 못찾을 경우 error 반환
            else:
                x.append(item)   # 변수(영어)가 아닐경우 정수나 상수이므로 x리스트에 append
        eval_result = self.evaluation(x)   # 후위 수식을 계산
        return eval_result  # 여기서, 수식은 후위 표기 수식임.
        # eval 명령어 수행 결과: 수식을 계산하여 그 결과값을 출력.

    def set(self, command):#  set 명령어 양식: “set 변수 수식 ;”
        command1 = command[1:]     # command[0] 부분은 딕셔너리에 저장할 변수이므로 인덱스 1부터
        oi = string.ascii_letters   # 후위 수식 계산
        x = []
        for item in command1:   # command1에는 set 과 딕셔너리에 저장할 변수 빼고 후위 수식만 있음
            if item in oi:     # 후위 수식에서 변수를 찾음
                if item in self.dicitems:   # 변수가 딕셔너리 키 값에 있을 경우
                    x.append(str(self.dicitems[item]))  # 키에 해당하는 value값 append
                else:
                    print("Error:", item, "is not defined")   # 변수를 못찾을 경우 error 반환
            else:
                x.append(item)    # 변수(영어)가 아닐경우 정수나 상수이므로 x리스트에 append
        self.dicitems[command[0]] = self.evaluation(x)   # 저장할 변수에 후위 수식 결과값 반환
        return self.dicitems
           # 여기서, 변수는 알파벳으로 시작하는 문자열이고, 수식은 후위 표기 수식임.

    def evaluation(self, expr):  # expr : list
        s = Stack()
        op = '+-*//%'  # op = ('+','-','*','/')
        for item in expr:   # 리스트의 원소를 하나씩 검사
            if item in op:   # 원소가 연사자일 경우 pop 두번해서 연산하고 다시 push 하는 과정
                right_opr = s.pop()     # 첫번째 원소 pop  두 번째 원소 pop
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
            elif item == ';':    # 원소가 세미콜론일 경우 for구문 break
                break
            else:
                s.push(int(item))  # 원소가 연산자가 아닐 경우는 이문제에서는 정수 와 상수뿐이므로 push
        if len(s.items) > 1:  # 스택에 원소가 남아 있을 경우
            return 'error2'    # 오류임
        else:
            return s.pop()   # 오류가 아닐경우 후위수식 결과값 pop해서 반환

    def switch(self, exprStr):  # 사용자의 입력을 공백 spilt해서 받아온 리스트를 정수 따로 연산자따로 변환해서 리스트화 하는 함수
        x = []
        op = '+', '*', '%', '-', ';'  # - 연산자는 - 정수부분 처리를 위해 따로 처리
        oi = '0123456789'  # // 연산자도 문자길이가 2이므로 따로 처리
        val = ''  # //와 - 연산자를 제외한 자머지 연사자를 처리하기 위한 변수
        val1 = ''  # // 연사자를 처리하기 위한 변수
        for c in exprStr:  # 리스트의 원소 한개씩 검사
            if len(c) == 1:  # 원소가 길이 한개 인 것들은 append함
                x.append(c)
            elif c[0] in '-':  # -(피연산자) 0보다 작은 정수의 경우는 스트링 [0]검사해서 '-'있으면 append
                x.append(c)
            elif len(c) > 1:  # 피연산자와 연산자가 붙어 있는 경우 떼어내는 부분
                for s in c:  # 한 글자씩 검사
                    if s in op:  # 한글자가 연산자일 경우
                        x.append(val)  # val변수는 연산자 이전에 숫자가 있을 경우 val에 저장하여
                        val = ''  # 연산자를 만날경우 숫자 반환하고 다시 초기화
                        x.append(s)  # 새로운 리스트 x에 append 하는 부분
                    elif s in oi:  # oi는 숫자임
                        val += s  # 숫자일 경우 val 변수에 string으로 이어 붙이기
                    elif s == '/':  # // 연산자도 길이가 2이므로 문자 한개씩 검사하 하다가 //만날경우
                        val1 += '/'  # 숫자 string 이어 붙이기와 같은 메커니즘으로 //가 될경우 append
                        if val1 == '//':
                            x.append(val1)  # 새로운 리스트 x에 append합니다.
                x.append(val)  # 그냥 길이가 1이상인 숫자만 있을 경우 val에 저장된 숫자 append
                val = ''
        while '' in x:
            x.remove('')  # x리스트 안에 ['']원소는 모두 삭제
        return x


def main():  # main() 바깥에서 실행해도 됨. 그냥 파이썬 처럼 해석됨.
    cal = Stack()   # stack 클래스 불러옴

    while True:
        com = input().split()   # com이라는 변수에 변수제거해서 spilt
        command = cal.switch(com[1:])    # 명령어 빼고 나머지 후위수식만 변수에 저장
        if com[0] == 'eval':          # eval 명령어
            print(cal.eval(command[:]))   # 후위 수식 결과값 출력
        elif com[0] == 'set':
            cal.set(command[:])
        elif com[0] == 'quit':
            break

if __name__ == '__main__':
    main()
