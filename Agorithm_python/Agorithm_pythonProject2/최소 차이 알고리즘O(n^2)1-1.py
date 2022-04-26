#              1.제목:한국외대 알고리즘 과제
#              2.날짜:20210929
# 문제 1-1
# 1) n(1이상 500000 이하 정수)개의 정수들에 대하여
# 두 수 차이의 최솟값을 출력하는 프로그램을 작성하시오. O(n2) 시간 알고리즘을 이용
n = int(input())  # n
n_list = list(map(int, input().split()))  # n 개의 정수
def selection_sort(arr):  # O(n^2)알고리즘인 선택 정렬 알고리즘을 이용
    for i in range(len(arr) - 1):  # 최소값의 index와 현재 index에 있는 값을 swap함.
        min_idx = i
        for j in range(i + 1, len(arr)):  # 현재 index부터 마지막 index까지
            if arr[j] < arr[min_idx]:   # 최소값의 인덱스를 찾아냄
                min_idx = j  # 각 index에 대해서 최소값을 찾기 위해 대소비교는 여러번
                             # 일어나지만 swap은 한번만 일어남.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def solution(n, n_list):
    selection_sort(n_list)   # n 개의 정수를 위의 선택 정렬 알고리즘으로 선택 정렬 시킴.
    num = list()    # 최소값을 출력하기위한 list
    for i in range(1, len(n_list)):    # n개 정수를 하나씩 검사
       j = n -1
       while j > i:
            if(n_list[j] > n_list[i]):
                num.append(n_list[j] - n_list[i])  # 두수의 차이를 num list에 append
            j -= 1  # j를 1씩 줄여가면서 n_list의 모든 i와 검사
    print(min(num))  # 최소값 출력
solution(n, n_list)
