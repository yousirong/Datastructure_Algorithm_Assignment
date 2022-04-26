#                1.제목:한국외대 자료구조 과제 5(5-1-1)
#                2.날짜:20210521
# 5-1-1) 교과목 수강자 관리를 위한 다음 명령어를 처리하는 프로그램을 작성하시오. 수강자는 학번정보(문자열)를 가진다.

class Node:
    def __init__(self, st_id):
        self.st_id = st_id  # 학번 data
        self.left = None   # 왼쪽 노드 선택
        self.right = None  # 오른쪽 노드 선택

class BSTree:
    def __init__(self):
        self.root = None  # root노드
        self.inorder_list = []   # 중위 순회해서 inorder_list에 대입
        self.count = []   # 노드의 개수를 새기 위한 count 변수

    def insert(self, st_id):   # 학번이 id인 학생이 수강신청을 함
        if self.root is None:   # 노드가 아무것도 없을 경우 root노드는 None인 상태
            self.root = Node(st_id)   # root노드에 처음 학번 노드 대입
        # root가 있으면 왼쪽배치 or 오른쪽배치
        else:
            self.__insert_node(self.root, st_id)  # root가 있을경우 어느 방향으로 배치 할 것인지 정해주는 __insert_node함수로 이동

        # root가 있는 경우
    def __insert_node(self, node, st_id):
        # root 값보다 작으면 왼쪽으로
        if node.st_id >= st_id:
            if node.left is not None:
                self.__insert_node(node.left, st_id)
            else:
                node.left = Node(st_id)
        # head 값보다 크면 오른쪽으로
        elif node.st_id < st_id:
            if node.right is not None:
                self.__insert_node(node.right, st_id)
            else:
                node.right = Node(st_id)
        else:
            return node.st_id

    def delete(self, st_id):  # 학번이 id인 학생이 수강신청을 취소함
        self.root, deleted = self._delete_value(self.root, st_id) # root노드가 None일 경우 deleted변수에 False담겨져 있음
        return deleted   # return False

    def _delete_value(self, node, st_id):
        if node is None:   # root노드가 None일 경우 못지움  -> return False
            return node, False
        deleted = False
        if st_id == node.st_id:    # 지우려는 st_id와 노드의 st_id가 같을 경우
            deleted = True
            if node.left and node.right:
                # node.right의 가장 왼쪽에있는 노드를 교체합니다.
                parent, child = node, node.right
                while child.left is not None:
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
        elif st_id < node.st_id:   # 지우려는 st_id보다 노드의 st_id 작을 경우 왼쪽으로 이동
            node.left, deleted = self._delete_value(node.left, st_id)
        else:                      # 지우려는 st_id보다 노드의 st_id 작을 경우 오른쪽으로 이동
            node.right, deleted = self._delete_value(node.right, st_id)
        return node, deleted

    def print_list(self):
        if self.root is not None:
            self.sizelist(self.root)

    def sizelist(self, node):  # list 크기 반환
        if node.left is not None:
            self.sizelist(node.left)

        self.count.append(node.st_id)

        if node.right is not None:
            self.sizelist(node.right)

    # 오름차순으로 출력 (중위)
    def in_order_traversal(self):
        self.inorder_list = []
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                self.inorder_list.append(root.st_id)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)
        int_li = sorted(self.inorder_list, key=str)
        # int_li = sorted(map(str, self.inorder_list))
        return int_li

classStudents = BSTree()
while True:
    command = input().split()
    if command[0] == 'N':  # st_id(즉, command[1])를 수강자리스트에 insert
        classStudents.insert(command[1])
    elif command[0] == 'C':  # st_id(즉, command[1])를 수강자리스트에서 delete
        classStudents.delete(command[1])
    elif command[0] == 'S':  # 수강자리스트의 원소 수를 출력
        classStudents.count = []
        classStudents.print_list()
        print(len(classStudents.count), end='\n')
    elif command[0] == 'P':  # 수강자리스트의 원소들을 오름차순으로 출력
        arr = classStudents.in_order_traversal()
        for i in arr:
            print(i, end=' ')

    elif command[0] == 'Q':  # 종료
        break
'''
N 111A
N 111B
N 111C
P
N 111-222
P
N 000-111
P 
C 111-222
P
'''
#  삽입되는 부분에서 문제있음
