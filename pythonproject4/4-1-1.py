#                1.제목:한국외대 자료구조 과제 4(4-1-1)
#                2.날짜:20210501
# 4-1)
# 과제 3-1-1)을 연결구조(linked stack)로 구현한 스택을 이용하여 프로그램을 작성하시오.
# ()[{a}]
# 1
# ()[{a}] {()]()
# 0
class Node:   # 노드 클래스
    def __init__(self, element):
        self.data = element
        self.link = None

class LinkedStack:
    def __init__(self):
        self.top = None  # 객체 초기화 함수

    def peek(self):
        if not self.isEmpty():
            return self.top.data   # stack이 비어있지 않을 경우 맨 앞 요소 리턴

    def isEmpty(self):
        return self.top == None

    def push (self, e):
        newNode = Node(e)
        newNode.link = self.top
        self.top = newNode

    def pop(self):
        if not self.isEmpty():
            e = self.top
            self.top = e.link
            return e.data

    def print(self):  # LinkedStack 출력
        if self.top is None:  # top이 비어있을 경우
            print("Linked list is empty")
        else:                 # top이 비어있지 않을 경우
            ele = self.top
            while ele is not None:
                if ele.link == None:
                    print(ele.data)
                else:
                    print(ele.data, '->', end='')
                ele = ele.link
        print("0")              # 예시 1->2->3->4

def solution(s):
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = LinkedStack()
    for c in s:   # input으로 문자열을 받아서 한 문자씩 루프
        if c in '({[':     # 한 문자가 열린괄호 일경우
            stack.push(c)  # 스택 리스트에 append
        elif c in ')}]':      # 한 문자가 닫힌괄호 일경우
            if stack:
                top = stack.pop()  # top 변수에 스택에 저장되어있는 제일 위의 문자 pop
                if d[c] != top:    # d 변수의 set에서 괄호의 짝이 아닐 경우
                    return False   # False 반환
            else:
                return False       # 위의 모든 경우 아닐 경우 반환
    return stack.isEmpty()          # 스택을 비움

p = input()
if(solution(p) == False):      # solution 함수에서 반환한 값이 False 일 경우
    print("0")                # 0출력
else:
    print("1")               # 반환 값이 True 일 경우 1출력


