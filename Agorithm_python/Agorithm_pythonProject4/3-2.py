from sys import stdin
# 행열 n, m 입력받기
# 첫 번째 줄에 사람들의 수 n(1이상 1,000이하 정수)와 친구 관계 수 m(0 이상 300,000 이하 정수)가 주어진다.
n, m = map(int, stdin.readline().split())
# 다음 m개의 각 줄에 친구 관계를 나타내는 두 사람의 번호가 주어진다.
arr = [[] for _ in range(n)]
for _ in range(m):
    hang, yeol = map(int, stdin.readline().split())  # 번호 입력받고 arr에 append
    arr[yeol].append(hang)
    arr[hang].append(yeol)
# 현재 arr는 친구관계 인접리스트(연결리스트)로 표현




def dfs(start, arr_visit):   # 탐색방법 : 깊이우선탐색
    people = 0   # 사람들
    stack = [start]   # 스택 이용
    while stack:   # 스택을 끝까지 도는 동안
        start = stack.pop()   # 첫 번째 시작값을 스택에 잇을 경우 pop해줌
        if start not in arr_visit:  # 만약 arr_visit에 방문하지 않았을 경우 방문처리
            arr_visit.append(start)  # arr_visit에 start append
            people += 1   # people변수에 사람들과 관계로 연결되어있으므로 people +1
            for x in arr[start]:  # arr에 관계 시작부분이 있을 경우 append
                stack.append(x)  # stack에 append
    return arr_visit, people   # 방문수, 사람들 리턴

visited_arr = []  # 방문한 사람 행렬
relship = 0  # 사람들과 연결되어 있는 집단의 수
ans = []  # 연결 되어있는 각 집단의 크기가 들어가있는 변수
if m !=0:  # m이 0인 경우가 0이 아닌 경우로 나눔
    for i in range(n):  # 입력 받은 n만큼 for구문 돌음
        visited_arr, people = dfs(i, visited_arr)  # 깊이 우선 탐색 돌음
        if people != 0:  # 만약 people이 0이 아닐 경우 관계수는 무조건 하나 이상 있음
            relship += 1
            ans.append(people)
else:  # 0인 경우
    people = 1  # 집단을 이루는 사람들은 무조건 1
    relship = n  # 집단은 n
    ans.append(people)
print(relship)   # 관계수
print(max(ans), min(ans))  # 가장 큰 집단의 크기, 가장 작은 집단의 크기를 출력하는 변수

'''
7 6
1 2
1 5
5 6 
5 2
0 4
2 3
'''