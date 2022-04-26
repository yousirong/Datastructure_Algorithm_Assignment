import sys
sys.setrecursionlimit(10**7)

class maze:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

m, n = map(int, input().split())  # m * n 크기 행렬 수 입력
maze_map = [[0 for _ in range(n)] for _ in range(m)]   # 미로
visit_road = [[False for _ in range(n)] for _ in range(m)]  # True는 방문 False는 미방문
# visit_road: 미로의 행과 열의 각 위치가 방문되었는지 아닌지를 확인하기 위한 2차원 배열
for i in range(m):
    x = input()   # 01입력 받아서
    maze_map[i] = list(map(int, list(str(x))))   # maze_map 행렬에 대입

# map: 미로 정보를 저장하는 2차원 배열
# 갈 수 있는 곳 1, 없는 곳 0
def dfs_maze(map, n, m, start, dest, visit_road): # start, dest: 출발지와 목적지
    next = maze() # class maze에서 행열 대입
    if map[start.x][start.y] == 1:  # 시작점이 1이라면
        visit_road[start.x][start.y] = True  # 시작 위치를 방문 했음 -> True
    else:  # 방문안했으면  -1
        return False   # 종료
    if start.x == dest.x:  # 시작 좌표가 목적지와 같다면 1 리턴
        return True   # 종료
    if start.x > 0: # 좌표에서 위쪽 이동 할 경우,y좌표가 m-1일 경우는 맨 밑줄 위치
        if map[start.x-1][start.y] == 1 and not visit_road[start.x - 1][start.y]:
            # 현재 좌료에서 위 행 이동  또는 방문처리 안된 경우
            next.x = start.x - 1   # 다음행 = 행 - 1
            next.y = start.y    # 다음행 = 열 + 0
            if dfs_maze(map, n, m, next, dest, visit_road):  # 함수실행가능 -> True일 때
                return True
    if start.y > 0: # 좌표에서 왼쪽 이동 할 경우
        if map[start.x][start.y-1] == 1 and not visit_road[start.x][start.y - 1]:
            # 현재 좌료에서 왼쪽 열 이동  또는 방문처리 안된 경우
            next.x = start.x   # 다음행 = 행 + 0
            next.y = start.y - 1   # 다음행 = 열 - 1
            if dfs_maze(map, n, m, next, dest, visit_road):  # 함수실행가능 -> True일 때
                return True
    if start.y < n-1:  # 좌표에서 오른쪽 이동 할 경우
        if map[start.x][start.y+1] == 1 and not visit_road[start.x][start.y + 1]:
            # 현재 좌료에서 오른쪽 열 이동  또는 방문처리 안된 경우
            next.x = start.x  # 다음행 = 행 + 0
            next.y = start.y + 1  # 다음 열 = 열 +1
            if dfs_maze(map, n, m, next, dest, visit_road):  # 함수실행가능 -> True일 때
                return True  #  True반환 종료
    if start.x < m-1:  # 좌표에서 아래 이동 할 경우
        if map[start.x+1][start.y] == 1 and not visit_road[start.x + 1][start.y]:
            # 현재 좌료에서 아래 행 이동  또는 방문처리 안된 경우
            next.x = start.x + 1  # 다음행 = 행 + 1
            next.y = start.y  # 다음 열 = 열 +0
            if dfs_maze(map, n, m, next, dest, visit_road):
                return True
    return False  # 동서남북 이동 불가 -> False

for i in range(n):
    result = dfs_maze(maze_map, n, m, maze(0, i), maze(m - 1, None), visit_road)
    if result:
        break

if result:  # result True, False 검사
    print(1)  # 가는길 있을 경우
else:
    print(-1)  # 가는 길 없을 경우

'''
6 10
0110000011
1101111101
1101010111
1111010111
0100111000
1011110111
'''