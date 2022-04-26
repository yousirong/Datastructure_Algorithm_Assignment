from collections import deque

m, n = map(int, input().split())  # m * n 크기 행렬 수 입력
maze_map = [[0 for _ in range(n)] for _ in range(m)]  # 미로
road = [[0 for _ in range(n)] for _ in range(m)]  # 01도로 입력
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(m):
    x = input()  # 01입력 받아서
    maze_map[i] = list(map(int, list(str(x))))  # maze_map 행렬에 대입
queue = deque()  # 너비우선탐색은 큐 이용

def bfs(maze_map, st_x, st_y):  # 탐색 방법 : 너비우선탐색
    visit_arr = [[False] * n for _ in range(m)]  # True는 방문 False는 미방문
    queue.append([st_x, st_y])  # 큐에 시작 좌표 append
    road[st_y][st_x] = 1  # 시작 좌표 방문했으므로 1로 처리
    while queue:
        x, y = queue.popleft()  # row와 col에 maze_map[0][i]를 넣음
        for i in range(4):  # 좌표계 위아래양옆을 동서남북으로 생각
            # 0 서, 1 북, 2 동, 3남
            X = x + dx[i]  # 이동한 x 좌표
            Y= y + dy[i]  # 이동한 y 좌표
            if 0 <= X < n and 0 <= Y < m and not visit_arr[Y][X]:
            # 만약 이동한 좌표가 입력 한 m*n안에 있고 visit_arr에 방문처리가 안되어있는 좌표라면
                if maze_map[Y][X] == 1:
                    visit_arr[Y][X] = True  # 방문처리
                    queue.append((X, Y))   # 새로운 좌표 큐에 append
                    road[Y][X] = road[y][x] + 1  # 위에서 방문처리한 그 지점까지의 거리를 원래 거리 +1
                    if Y == m - 1:  # y좌표가 m-1일 경우는 맨 밑줄 위치
                        queue.clear()  # 큐 비우고
                        return road[Y][X]  # 거리값 리턴턴
new_list = []

for i in range(n):
    if maze_map[0][i] == 1:
        new_list.append(bfs(maze_map, i, 0))
res = list(filter(None, new_list))  # bfs함수를 돌은 거리값들을 새로운 결과변수에 filter 함수 이용해서 정리
if len(res) == 0:  # res가 0이라면 갈수 없는 좌표이다.
    print(-1)  # 가는 길이 없는 경우 -1출력
else:
    print(min(res))  # 가는 길이 있으면 최소 결과값 출력