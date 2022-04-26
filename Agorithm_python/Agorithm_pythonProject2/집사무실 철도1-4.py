#              1.제목:한국외대 알고리즘 과제
#              2.날짜:20210929
# 문제 1-4
# 양의 정수 𝑑와 𝑛 개의 정수 쌍, (), ,이 주어져 있다. 여기서 와 는 각각 사람 𝑖의 집과 사무실의 위치이다.
# 길이 𝑑의 모든 선분 𝐿에 대하여, 집과 사무실의 위치가 모두 𝐿에 포함되는 사람들의 최대 수를 구하는
# 프로그램을 작성하시오.

# 첫 번째 줄에 사람 수 이 주어진다. 다음 개 각 줄에 정수 쌍 ()가 주어진다.
# 여기서 와 는 -100,000,000 이상 100,000,000 이하의 서로 다른 두 정수이다.
# 마지막 줄에 철로의 길이를 나타내는 정수 가 주어진다.

import sys
import heapq
# 각 경로를 순회하면서 집, 사무실중 좌표값이 큰 점에서 왼쪽으로 d 길이의 철로를 깔았을 때
# 철로를 깔았을 때 철로에 몇 개의 경로가 포함되는지를 확인하는 방식
n = int(sys.stdin.readline())
road_info = []  # 입력받은 철도 저장하는 철도 정보
result = 0  # 결과값
hp = []   # heap
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))  # 입력받은 순서대로 enter를 기준으로 좌표선분 mapping
    road_info.append(road)  # road_info 배열에 좌표 선분 append

d = int(sys.stdin.readline())   # 길이 d
roads = []   # 오름 차순으로 정렬된 road를 저장함
for road in road_info:
    house, office = road  # 각 사무실, 집 정보를 road에 저장할 때
    if abs(house - office) <= d:  # 사무실과 집의 거리가 d 보다 크다면 포함될 수 없으므로 저장x
        road = sorted(road)  # d보다 작거나 같다면 좌표정보를 오름차순으로 정렬
        roads.append(road)
roads.sort(key=lambda x:x[1])  # 철로의 시작점을 가장 작은 것부터 시작할 수 있도록 road을
                               # 입력된 원소 중 큰 원소를 기준으로 오름차순 정렬

for road in roads:  # 철로의 시작점을 가장 작은 것부터 순회하면서 차례대로 힙에 저장
    if hp:
        while hp[0][0] < road[1] - d:   # 힙에 존재하는 가장 작은 값이 철로의 끝점안에 있는지 확인
            heapq.heappop(hp)   # 철로 내에 있지 않다면 힙에서 pop
            if not hp:
                break
        heapq.heappush(hp, road)

    else:  # if hp
        heapq.heappush(hp, road)
    result = max(result, len(hp))
print(result)

'''
8	       
5 40
35 25
10 20
10 25
30 50
50 60
30 25
80 100
30
'''
'''
4	       
20 80
70 30
35 65
40 60
10
'''