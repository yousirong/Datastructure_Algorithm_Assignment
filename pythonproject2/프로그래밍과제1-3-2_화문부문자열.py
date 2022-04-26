# 3-2) 문자열 s의 서로 다른 모든 회문 부문자열(substring)을 사전식 순서대로 출력하는 프로그램을 작성하시오.
# 단, 대/소문자 구분하지 않으며, 출력하는 회문 부문자열의 각 문자는 소문자이다.
# sort 함수를 사용하여도 좋음)

# 단, 문자열이 회문인지 판별하는 함수를 정의하고 이를 사용하여야 함

# 입력 예 1
# absAba

# 출력 예 2
# a aba b s

from collections import OrderedDict


def logestPalindrome(s: str) -> str:    # 회문을 판별하기 위해 함수를 2중으로, 하나는 회문 판별 다른하나는 부분문자열
    def expand(left: int, right: int) -> str:
        # 팰린드롬 여부를 체크하며 포인터 확장
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        # 팰린드롬은 짝수, 홀수 경우 모두 나타나기 때문에 2가지 형태의 포인터 사용
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)

    return result

s = input()
s = s.lower()  # 입력받은 회문 소문자로 변환


s1 = logestPalindrome(s)    # 회문 부분문자열 함수


s_output = (''.join(OrderedDict.fromkeys(s)))   # OrderedDict라는 함수를 사용하여 한글자여도 회문인 글자를 추출

a = list(str(s_output))  # 회문 인 부분문자열과 list를 합침
a.append(s1)

b = sorted(a)   # 오름차순으로 정렬

print(' '.join(b))
# 1번 케이스만 성공
# 부분 문자열
