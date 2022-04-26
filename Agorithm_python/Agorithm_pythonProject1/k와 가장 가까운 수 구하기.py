#              1.제목:한국외대 알고리즘 과제
#              2.날짜:20210911
# 3) 오름차순으로 정렬된 n(2이상 100,000이하 정수)개의 정수(1,000,000,000이하 정수) 중
# K(정수)와 가장 가까운 정수를 찾는 프로그램을 작성하시오. K와 가장 가까운 정수가 여러 개일 경우, 이들 중 큰 수를 출력하시오.

# 요구 조건: 이진탐색(binary search)을 이용해야 한다.

n = int(input())  # n
num_list = list(map(int, input().split()))  # n개의 정수
k = int(input())  # k


def solve(n,num_list,k):
    num_list.sort()  # 정렬
    left = 0
    right = len(num_list) - 1
    while left <= right:  # left가 right보다 클 때까지 진행하는 while문
        if 2 <= n <= 100000:
            mid = (left + right) // 2  # 배열의 중간에 있는 임의의 값
            if k == num_list[mid]:  # 구하고자 하는 k가 리스트의 중간값과 같다면 k를 리턴하고 종료
                return num_list[mid]
            elif k < num_list[mid]:
                right = mid - 1  # else와 elif 부분은 교재 이진탐색 참고함.
            elif k > num_list[mid]:
                left = mid + 1
            else:
                break
    # left가 right보다 커지면 종료
    if k not in num_list:  # num_list에 k가 없을 경우에
        low_num = abs(k - num_list[right])  # 현재 right의 인덱스가 더 작으므로,
        # 작은 인덱스쪽의 절대값을 k - num_list[right]으로 줬고 이를 low_num로 선언
        high_num = abs(num_list[left] - k)  # 현재 left의 인덱스가 더 크므로,
        # 큰 인덱스쪽의 절대값을 num_list[left] - k로 줬고 이를 high_num로 선언
        # print(low_num, high_num)
        if low_num < high_num:  # 더 작은 인덱스의 절대값이 더 큰 인덱스의 절대값보다 같거나 작을 때:
            result = num_list[right]  # 결과값 result에 num_list[right]을 부여함
        elif low_num > high_num:  # 더 작은 인덱스의 절대값이 더 큰 인덱스의 절대값보다 클 때:
            result = num_list[left]  # 결과값 result에 num_list[left]을 부여함
        elif low_num == high_num:
            result = num_list[right+1]
        return result  # 최종 결과값 result를 반환합니다.


print(solve(n, num_list, k))

'''
5
20 30 40 55 60
36
'''
'''
중간값 : 40 -> 작다 -> {20,30}
중간값 : 30 -> 크다 -> 종료
N개의 크기 배열을 이진 탐색하면 N, N/2, N/8,...,1으로 실행 됨.
이진 탐색의 시간 복잡도는 O(logN)입니다.

'''
'''
5
20 30 40 55 60
35
'''
