from collections import deque
class maze:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visit_arr = [[False] * n for _ in range(m)]  # True는 방문 False는 미방문

m, n = map(int, input().split())  # m * n 크기 행렬 수 입력
maze_map = [[0 for _ in range(n)] for _ in range(m)]  # 미로
road = [[0 for _ in range(n)] for _ in range(m)]  # 01도로 입력
# visit_arr = [[False for _ in range(n)] for _ in range(m)]  # True는 방문 False는 미방문
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(m):
    x = input()  # 01입력 받아서
    maze_map[i] = list(map(int, list(str(x))))  # maze_map 행렬에 대입
queue = deque()  # 너비우선탐색은 큐 이용

def bfs(maze_map, start, dest):  # 탐색 방법 : 너비우선탐색
    next = maze()
    # start.x, start.y  i, 0
    # visit_arr = [[False] * n for _ in range(m)]  # True는 방문 False는 미방문
    if maze_map[0][start.x] == 1:  # 시작점이 1이라면
        # visit_arr[start.x][start.y] = True
        queue.append([start.x, start.y])  # 큐에 시작 좌표 append
        road[start.y][start.x] = 1  # 시작 좌표 방문했으므로 1로 처리
    else:
        return False
    # if start.x == dest.x:  # 시작 좌표가 목적지와 같다면 1 리턴
    #     return True  # 종료
    while queue:
        start.x, start.y = queue.popleft()  # row와 col에 maze_map[0][i]를 넣음
        for i in range(4):  # 좌표계 위아래양옆을 동서남북으로 생각
            # 0 동, 1 북, 2서, 3남
            next.x = start.x + dx[i]  # 이동한 x 좌표
            next.y = start.y + dy[i]  # 이동한 y 좌표
            if 0 <= next.x < n and 0 <= next.y < m and not next.visit_arr[next.y][next.x]:
            # 만약 이동한 좌표가 입력 한 m*n안에 있고 visit_arr에 방문처리가 안되어있는 좌표라면
                if maze_map[next.y][next.x] == 1:
                    next.visit_arr[next.y][next.x] = True  # 방문처리
                    queue.append([next.x, next.y])   # 새로운 좌표 큐에 append
                    road[next.y][next.x] = road[start.y][start.x] + 1  # 위에서 방문처리한 그 지점까지의 거리를 원래 거리 +1
                    if next.y == dest.y:  # 좌표에서 위쪽 이동 할 경우,y좌표가 m-1일 경우는 맨 밑줄 위치
                        queue.clear()  # 큐 비우고
                        return road[next.y][next.x]  # 거리값 리턴


new_list = []
for i in range(n):

    new_list.append(bfs(maze_map, maze(i, 0), maze(None, m-1)))
res = list(filter(None, new_list))  # bfs함수를 돌은 거리값들을 새로운 결과변수에 filter 함수 이용해서 정리
# print(res)
if len(res) == 0:  # res가 0이라면 갈수 없는 좌표이다.
    print(-1)  # 가는 길이 없는 경우 -1출력
else:
    print(min(res))  # 가는 길이 있으면 최소 결과값 출력

'''
6 10
0110000011
1101111101
1101010111
1111010111
0100111000
1011110111
'''