#              1.제목:한국외대 알고리즘 과제
#              2.날짜:20210929
# 문제 1-2
# 2) n(1이상 500000 이하 정수)개의 정수들에 대하여
# 두 수 차이의 최솟값을 출력하는 프로그램을 작성하시오.
# 정렬을 이용하고, 정렬 알고리즘은 병합정렬을 사용한다.

n = int(input())  # n
n_list = list(map(int, input().split()))  # n 개의 정수
def merge_sort(arr):  # 재귀를 이용해서 병합 정렬 구현
    if len(arr) < 2:  # 재귀 알고리즘의 기저 조건
        return arr    # 입력 배열 의 크기가 2보다 작을 때
                      # 이 조건에 해당 되면 배열을 그대로 반환
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])   # mid원소 기준 왼쪽 배열 재배치
    right_arr = merge_sort(arr[mid:])   # mid 원소 오른쪽 배열 재배치

    merged_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr):  # 원소 1개로 쪼개고 난 후 합칠 때는
        if left_arr[l] < right_arr[h]:              # 작은 숫자가 앞에 큰 숫자를 뒤에 위치
            merged_arr.append(left_arr[l])
            l += 1
        else:                             # 큰 숫자가 앞에 작은 숫자가 뒤에 위치
            merged_arr.append(right_arr[h])
            h += 1
    merged_arr += left_arr[l:]
    merged_arr += right_arr[h:]
    return merged_arr

def solution(n, n_list):
    new_n_list = merge_sort(n_list)   # n개의 정수를 병합정렬함
    num = list()
    for i in range(0, n-1):
        if(new_n_list[i+1] >= new_n_list[i]):
          if(len(num)==0):   # num리스트에 아무것도 없을때 그냥 대입
               num.append(new_n_list[i+1] - new_n_list[i])
          else:              # num리스트가 none이 아닐 경우
               x = new_n_list[i+1] - new_n_list[i]
               if(num[0] >x):   # num에 추가된 차이값보다 x가 작을 경우 append
                   num.append(x)
    print(min(num))   # num리스트에서 최솟값 출력

solution(n, n_list)
'''
10
1 10 20 7 15 30 40 50 32 5
'''

