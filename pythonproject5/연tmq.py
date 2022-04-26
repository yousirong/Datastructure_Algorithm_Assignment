#                1.제목:한국외대 자료구조 과제 5(5-1-2)
#                2.날짜:20210526
# 2) 서점의 도서 재고관리 프로그램을 작성하시오.
from operator import itemgetter


class Node:
    # st_id 도서번호, title 도서이름, price 가격, num 수량
    def __init__(self, st_id, title, price, num):
        self.st_id = st_id  # 도서번호
        self.title = title  # 도서이름
        self.price = price  # 가격
        self.num = num  # 수량
        self.book = [self.st_id, self.title, self.price, self.num]  # book이라는 리스트를 만들어
        # 입력한 것들을 모두 포함하는 도서정보를 만듬듬
        self.left = None  # 왼쪽 트리
        self.right = None  # 오른쪽 트리


class BSTree:
    def __init__(self):
        self.root = None  # 루트 노드
        self.root1 = None
        self.sellbook_list = []  # 판매한 모든 도서의 판매정보
        self.order_list = []  # 오름차순으로 출력하는 리스트
        self.count = []  # 노드 개수 세는 변수

    def insert(self, st_id, title, price, num):  # 입력: 도서번호, 도서이름, 가격, 입고수량
        if self.root is None:  # 루트 노드가 None일 경우(노드가 없을 경우)
            self.root = Node(st_id, title, price, num)  # root노드에 첫번째 노드 insert
            self.root.book = [st_id, title, price, num]  # 도서 목록
        # root가 있으면 왼쪽배치 or 오른쪽배치
        else:
            if self.root.book[0] == st_id:
                return print("error: 1")  # 유의사항: 신규도서가 재고도서 목록에 있을 경우 “error: 1” 출력
            else:
                self.__insert_node(self.root, st_id, title, price, num)  # 왼쪽, 오른쪽 자식노드 결정하는 함수로 이동
        # root가 있는 경우

    def __insert_node(self, node, st_id, title, price, num):  # 왼쪽, 오른쪽 자식노드 결정하는 함수
        # root 값이 크면 왼쪽으로
        if node.st_id > st_id:  # 왼쪽 자식 노드
            if node.left is not None:
                self.__insert_node(node.left, st_id, title, price, num)
            else:
                node.left = Node(st_id, title, price, num)
        # root 값이 작으면 오른쪽으로
        elif node.st_id < st_id:  # 오른쪽 자식 노드
            if node.right is not None:
                self.__insert_node(node.right, st_id, title, price, num)
            else:
                node.right = Node(st_id, title, price, num)
        elif node.st_id == st_id:  # 유의사항: 신규도서가 재고도서 목록에 있을 경우 “error: 1” 출력
            return print("error: 1")
        else:
            return node.st_id

    def addbook(self, st_id, num):  # 재고도서 목록에 있는 도서 입고
        if self.root.st_id is None:
            return print("error: 2")  # 유의사항: 도서번호의 도서가 재고도서 목록에 없을 경우 “error: 2” 출력
        else:
            return self.__add_book(self.root, st_id, num)  # 왼쪽, 오른쪽 자식노드에서 st_id 찾는 함수

    def __add_book(self, node, st_id, num):
        if node.st_id == st_id:  # 왼쪽 자식 or 오른쪽 자식 노드에서 입력한 학생 번호와 일치 할 경우
            node.book[3] = str(int(node.book[3]) + int(num))  # 도서 입고후 더하는 부분
            return True
        else:
            if node.st_id > st_id:  # 왼쪽 자식 일 경우
                if node.left is not None:
                    return self.__add_book(node.left, st_id, num)
                else:
                    return print("error: 2")
            if node.st_id < st_id:  # 오른쪽 자식 일 경우
                if node.right is not None:
                    return self.__add_book(node.right, st_id, num)
                else:
                    return print("error: 2")

    # 판매한 모든 도서의 판매정보(도서번호, 도서이름, 가격, 판매수량)를 도서번호 오름차순으로 출력
    def sellbook(self, st_id, num):  # 재고도서 목록에 있는 도서를 판매함
        if self.root.st_id is None:  # 재고도서 목록 root가 None일 경우(도서목록에 도서 없는 경우)
            return print("error: 2")  # 유의사항: 입력되는 도서번호가 재고도서 목록에 없을 경우, “error: 2”
        else:  # 재고도서 목록 root에 노드가 있는 경우
            return self.__sell_book(self.root, st_id, num)  # 왼쪽자식, 오른쪽자식노드로 이동하는 함수

    def __sell_book(self, node, st_id, num):  # 왼쪽자식, 오른쪽자식노드로 이동하는 함수
        # root 값보다 작은 왼쪽자식으로
        if node.st_id > st_id:  # 왼쪽 자식 일 경우
            if node.left is not None:
                return self.__sell_book(node.left, st_id, num)
            else:
                return print("error: 2")
        # root 값보다 크면 오른쪽자식으로
        elif node.st_id < st_id:  # 오른쪽 자식 일 경우
            if node.right is not None:
                return self.__sell_book(node.right, st_id, num)
            else:
                return print("error: 2")
        elif node.st_id == st_id:  # 판매하려는 학생번호와 노드의 학생번호가 일치 할 경우
            if int(node.book[3]) < int(num):  # 판매수량이 재고 수량보다 많을 경우
                return print("error: 3")  # 판매수량이 재고수량보다 많을 경우 “error: 3” 출력
            else:  # 판매수량이 재고수량보다 작을 경우(판매할 수 있는 경우)
                node.book[3] = str(int(node.book[3]) - int(num))  # 도서목록에서 num(판매하려는 도서)만큼 뺌
                if len(self.sellbook_list) == 0:  # 판매한 모든 도서의 판매정보가 없을 경우
                    self.sellbook_list += [st_id, node.title, node.price, num]  # 판매 정보 입력
                else:  # 판매한 도서의 판매정보가 있을경우
                    for i in self.sellbook_list:  # 리스트의 한단어씩 검사함
                        if i == st_id:  # 검사해서 같은 도서를 또 파는 경우
                            n = int(self.sellbook_list.index(i))
                            if n == 0:
                                p = 3
                            else:
                                p = n + 3  # 도서수량의 인덱스는 3 7 11 .... 점화식임
                            self.sellbook_list[p] = str(int(self.sellbook_list[p]) + int(num))  # 기존판매수량 +판매수량
                            return True
                    self.sellbook_list += [st_id, node.title, node.price, num]

    def delete(self, st_id):  # 도서 폐기 (재고도서 목록에서 완전히 삭제함)
        self.root, deleted = self._delete_value(self.root, st_id)
        return deleted

    def _delete_value(self, node, st_id):
        if node is None:  # 도서목록에 삭제하려는 도서 없을 경우 == root에 노드 없을 경우
            print("error: 2")
            return node, False
        deleted = False
        if st_id == node.st_id:  # 삭제하려는 노드와 도서번호가 같을경우
            deleted = True
            if node.left and node.right:
                # node.right의 가장 왼쪽에있는 노드를 교체합니다.
                parent, child = node, node.right
                while child.left is not None:  # 왼쪽 자식 노드가 없을경우
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif st_id < node.st_id:  # 삭제하려는 도서번호가 비교하는 노드보다 작을 경우
            node.left, deleted = self._delete_value(node.left, st_id)
        elif st_id > node.st_id:  # 삭제하려는 도서번호가 비교하는 노드보다 클 경우
            node.right, deleted = self._delete_value(node.right, st_id)
        return node, deleted

    def inquirybook(self, st_id):  # 재고도서 목록에 있는 도서 입고
        if self.root.st_id is None:
            return print("error: 2")  # 유의사항: 입력되는 도서번호가 도서재고 목록에 없을 경우 “error: 2” 출력
        else:
            return self.__inquiry_book(self.root, st_id)

    def __inquiry_book(self, node, st_id):  # 왼쪽, 오른쪽 자식노드에서 st_id 찾기
        if node.st_id == st_id:
            print(' '.join(node.book), end=' ')  # 도서번호 일치할경우 해당 도서 출력
            return True
        else:
            if node.st_id > st_id:
                if node.left is not None:
                    return self.__inquiry_book(node.left, st_id)
                else:
                    return print("error: 2")
            elif node.st_id < st_id:
                if node.right is not None:
                    return self.__inquiry_book(node.right, st_id)
                else:
                    return print("error: 2")

    def print_list(self):  # 도서재고 목록에 있는 모든 도서의 재고상태(도서번호, 도서이름, 가격, 재고수량)를 도서번호 오름차순으로 출력
        if self.root is not None:
            self.sizelist(self.root)  # 왼쪽, 오른쪽 자식 노드에서 찾는 함수

    def sizelist(self, node):  # 왼쪽, 오른쪽 자식 노드에서 찾는 함수
        if node.left is not None:  # 노드를 리스트에 append 한후 개수를 샙니다.
            self.sizelist(node.left)
        self.count.append(node.st_id)
        if node.right is not None:
            self.sizelist(node.right)

    # 도서재고 목록에 있는 모든 도서의 재고상태(도서번호, 도서이름, 가격, 재고수량)를 도서번호 오름차순으로 출력
    def in_order_traversal(self):
        self.order_list = []

        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                self.order_list.append(root.book)
                _in_order_traversal(root.right)

        _in_order_traversal(self.root)
        int_li = sorted(self.order_list, key=str)
        return int_li

    def list_chunk(self, lst, n):  # 리스트를 일정한 수를 반복해서 자르는 함수 -> 중첩 리스트로 만들어줌
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    def L_listprint(self):  # 판매한 모든 도서의 판매정보(도서번호, 도서이름, 가격, 판매수량)를 도서번호 오름차순으로 출력
        int_li = self.list_chunk(self.sellbook_list, 4)  # 리스트를 4개씩 잘라서 중첩리스트 만듬
        int_li.sort(key=itemgetter(0))  # 인데스 0를 기준으로 리스트를 정렬함
        for item in int_li:
            print(' '.join(item), end='\n')


classStudents = BSTree()
while True:
    command = input().split()
    if command[0] == 'N':  # 신규도서 입고
        classStudents.insert(command[1], command[2], command[3], command[4])
    elif command[0] == 'D':  # 도서 폐기 (재고도서 목록에서 완전히 삭제함)
        classStudents.delete(command[1])
    elif command[0] == 'R':  # 재고도서 목록에 있는 도서 입고
        classStudents.addbook(command[1], command[2])
    elif command[0] == 'S':  # 재고도서 목록에 있는 도서를 판매함
        classStudents.sellbook(command[1], command[2])
    elif command[0] == 'I':  # 도서의 재고 상태 조회
        classStudents.inquirybook(command[1])
    elif command[0] == 'L':  # 수강자리스트의 원소 수를 출력
        arr = classStudents.L_listprint()
    elif command[0] == 'P':  # 수강자리스트의 원소들을 오름차순으로 출력
        arr = classStudents.in_order_traversal()
        for i in arr:
            print(' '.join(i), end='\n')
    elif command[0] == 'Q':  # 종료
        break
