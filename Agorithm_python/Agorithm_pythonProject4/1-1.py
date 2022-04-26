import sys
sys.setrecursionlimit(10000)
def has_duplicates(seq):  # 중복인지 아닌지 판별해주는 함수
    return len(seq) != len(set(seq))

def dfs(i, n, arr,visited):  # 탐색 방법: 깊이 우선 탐색
    visited[i] = True   # 0부터 n까지 입력받은 시작 위치 i, 시작위치는 방문했다고 표시 True
    result.append(i)   # result 배열에 현재 방문하고 있는 위치 append
    #print(result)
    if i - arr[i] >=0:    # 시작위치 - i번째 배열값 >=0
        if i == n-1 and arr[-1] > 0:   # 1차원 배열에서 마지막 배열 값이 0보다 큰경우 -> 왼쪽 으로 이동 가능
            result.append(i)   # result배열에 append
            return result
        if visited[i - arr[i]] is False:   # visited배열에서 이미 방문한 배열인지 아닌지 판단
            return dfs(i-arr[i],n,arr,visited)   # 깊이우선탐색 recursion
    if i+arr[i] < n:  # 시작위치 + i번째 배열값 < n
        if i == n-1 and arr[-1] > 0:  # 1차원 배열에서 마지막 배열 값이 0보다 큰경우 -> 왼쪽 으로 이동 가능
            result.append(i)  # result배열에 append
            return result
        if visited[i + arr[i]] is False:   # visited배열에서 이미 방문한 배열인지 아닌지 판단
            return dfs(i+arr[i],n,arr,visited)  # 깊이우선탐색 recursion
    return False   # 위의 if 구문 모두 해당 안될 경우 break

n = int(sys.stdin.readline())  # 1차원 배열 길이 입력
result=[]   # 검사용  # 방문하고 있는 위치를 담는 list
result_num =[0] *n   # 마지막으로 방문한 index의 배열값을 시작위치 index에 입력 받는 0으로 구성된 list
num = list(map(int, sys.stdin.readline().split()))  # 1차원 셀 각각의 셀값 입력
arr = [0 for i in range(n)]  # arr에는 최소값이 들어감
for i in range(n):
    arr[i] = num[i]   # num값을 arr배열에 대입

for startPosition in range(n):
    result = []   # result배열 초기화
    visited = [False] * n   # visited 방문처리 확인하는 배열 False로 초기화 -> 방문처리될 경우 True
    for i in range(startPosition):  # 0부터 n까지 시작위치
        visited[i] = True  # 시작위치는 함수 방문하기 전에 방문한것으로 표시
    dfs(startPosition, n, arr, visited)  # 깊이 우선 탐색 함수
    if len(result) != 1:   # bfs 함수를 1번이상 돌경우 배열의 길이는 1이상
        result_num[startPosition] = result[-1]  # 시작위치의 가장 많은 간 셀 값을 반환
    else:  # bfs함수를 안돌 경우 result 배열의 길이는 0
        result_num[startPosition] = 0
    #print("최종답안",result_num)

if has_duplicates(result_num) is False:  # list 중복되는 값 없을 경우-> False
    print(result_num.index(max(result_num)))
elif has_duplicates(result_num) is True:  # list에 중복 되는 값 있을 경우-> True
    pos = []
    for i in range(len(result_num)):
        if result_num[i] == max(result_num):  # 최대값일 경우 append
            pos.append(i)
    for i in pos:
        print(i, end=' ')  # 한 줄로 print
'''
10  
3 6 4 1 3 4 2 5 3 0
'''
'''
10  
1 1 1 1 1 1 1 1 1 1
'''
