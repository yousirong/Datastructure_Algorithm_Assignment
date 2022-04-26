#                1.제목:한국외대 자료구조 과제 4(4-1-2)
#                2.날짜:20210501
# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때,
# 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하시오.

# **** 배열 큐가 아닌 LinkedQueue로 구했습니다. ****
'''
4 2 10
7 4 5 6
'''
'''
8
'''
class Node:
    def __init__(self, element):
        self.data = element
        self.link = None
class Queue:
    def __init__(self):
        self.front = self.rear = None   # data 받기 전에는 front, rear는 None 상태

    def isEmpty(self):
        return self.front == None  # front가 None일 경우 data 아무것도 없음

    def enqueue(self, e):
        newNode = Node(e)
        if self.front == None:
            self.front = self.rear = newNode
        else:
            self.rear.link = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue empty")
            return 0
        e = self.front.data
        self.front = self.front.link
        if self.front == None:
            self.rear = None
        return e

    def peek(self):
        if self.isEmpty():
            print("Queue empty")
        else:
            return self.front.data   # self.front 만 리턴하면 type이 node가 됨
        # 그러므로 self.front.data로 element를 뽑아냄
answer = input().split(" ")  # n ==  다리를 건너는 트럭의 수 w == 다리의 길이 L ==  다리의 최대하중
                             # 세 개의 정수 n(1≤n≤1000), w(1≤w≤100), L(10≤L≤1000)
tmp = input().split(" ")   # 입력의 두 번째 줄에는 n개의 정수 a1, a2, ..., an이 주어지는데,
                           # ai는 i번째 트럭의 무게를 나타낸다.

truck = Queue()   # truck변수와 bridge변수 Queue 클래스에 연결
bridge = Queue()
time = 0     # 최단시간
bridge_sum = 0  # 최대 하중

for i in tmp:
    truck.enqueue(int(i))
for i in range(int(answer[1])):
    bridge.enqueue(0)  # 다리무게가 0 인 트럭을 세워놓고 enqueue하면 트럭의 무게를 할당해주는 방식으로 풀어냈습니다.

while not bridge.isEmpty():
    if truck.isEmpty():  # bridge를 할당했지만 truck이 비어 있을 경우
        bridge.dequeue()  # bridge를 dequeue함.
    else:                 # bridge 할당하고 truck무게도 할당했을 경우
        bridge_sum -= bridge.dequeue()  # 최대 하중 = 최대하중 - 브릿지 하중

        if bridge_sum + truck.peek() <= int(answer[2]):  # 최대하중 + 맨앞 트럭 무게가 그다음 무게의 트럭보다 작을 경우
            tmp = truck.dequeue()    # 그다음 트럭 dequeue
            bridge_sum += tmp        # 브릿지 최대하중에 건너는 트럭 무게 더함
            bridge.enqueue(tmp)      # 트럭이 건너면 브릿지 무게 enqueue
        else:
            bridge.enqueue(0)        # 브릿지 최대하중 못버팀
    time += 1                        # 트럭 건널때마다 time++

print(time)

