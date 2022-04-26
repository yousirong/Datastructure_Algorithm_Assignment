#                1.제목:한국외대 자료구조 과제 4(4-1-3)
#                2.날짜:20210504
# 4-3) (간단한 연결리스트 만들기 연습)
class Node:
    def __init__(self, element):
        self.data = element
        self.link = None

class StList:
    def __init__(self):
        self.head = None

    def isempty(self):   # 노드의 개수를 반환 해주는 함수에서 반환 값이 0인 경우
        if self.sizelist() != 0:
            return False  # 비어있지 않음 -> False
        else:
            return True   # 비어있음 ->True

    def insert(self, st_id):   # 교수님께 피드백 받은 대로 노드 삽입하는
        # 부분에서 새로운 data를 받을 때 마다 head 다음 첫 노드로 연결합니다.
        newnode = Node(st_id)
        newnode.link = self.head
        self.head = newnode
        # newnode = Node(st_id)   # 새로받은 data를 노드 끝에 연결하는 것은 주석 처리했습니다.
        # if self.head is None:
        #     self.head = newnode
        # else:
        #     cur = self.head
        #     while cur.link is not None:
        #         cur = cur.link
        #     cur.link = newnode

    def delete(self, st_id):
        # 지우는 값이 맨 앞 부분 일 때
        if self.head.data == st_id:
            tmp = self.head
            self.head = self.head.link
            del tmp
        else:
            # 지우는 값이 중간값일때
            node = self.head
            while node.link:
                if node.link.data == st_id:
                    temp = node.link
                    node.link = node.link.link
                    del temp
                    return
                else:
                    node = node.link

    def sizelist(self) -> int:  # list 크기 반환
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.link
        return count

    def print(self):
        arr1 = []
        newfound = self.head
        while newfound:
            if newfound.link is not None:
                arr1.append(newfound.data)
                newfound = newfound.link
            else:
                arr1.append(newfound.data)
                newfound = newfound.link
        int_li = sorted(arr1, key=str)  # 맨 앞자리 수 기준 으로 정렬 key =str 이용
        # int_li = sorted(map(str, arr1))
        return int_li


L = StList()
while True:
    command = input().split()
    if command[0] == 'N':  # st_id(즉, command[1])를 수강자리스트에 insert: L.insert(command[1])
        L.insert(command[1])
    elif command[0] == 'C':  # st_id(즉, command[1])를 수강자리스트에서 삭제: L.delete(command[1])
        L.delete(command[1])
    elif command[0] == 'S':  # 수강자리스트의 원소 수를 출력: L.size() 출력
        print(L.sizelist())  # L.size하면 int형을 반환 할 수 없다고 에러나서 sizelist로 이름 변경했습니다.
    elif command[0] == 'P':  # 수강자리스트의 원소들을 오름차순으로 출력: L.print()
        arr = L.print()  # L.print()
        for i in arr:
            print(i, end=' ')
    elif command[0] == 'Q':  # 종료
        break
# 교수님께 질문 드렸던 delete 부분과 다른 학우가 질문했던 8번 케이스인 ex) 111-113 처리하는 부분을 고쳤습니다.
# 입력 예
'''
N 111B
N 111A
N 111C


N 111D
S
P
Q
'''
# 출력결과
'''
4                # S
1111 1113 1115  # P
3                # S
1111 1112 1113 1115 # P
'''