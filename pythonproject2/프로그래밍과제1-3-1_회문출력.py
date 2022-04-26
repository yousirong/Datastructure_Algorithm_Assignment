#              1.제목:한국외대 자료 구조 과제
#              2.날짜:20210315
# 3-1) 문자열이 회문이면 yes를 출력하고 그렇지 않으면 no를 출력하는 프로그램을 작성하시오. (대/소문자 구분하지 않음)
#
# 단, 문자열이 회문인지 판별하는 함수를 정의하고 이를 사용하여야 함
#
# 입력 예 1
# absBa
#
# 출력 예 1
# yes
#
# 입력 예 2
# absaba
#
# 출력 예 2
# no

def Palindromedis(string):     # 회문 판별 Palindrome discrimination
    palin = string.lower()     # 받은 단어를 소문자로 변경
    for i in range(0, len(palin)//2):   # 단어의 길이의 반 값을
        if palin[i] != palin[-(i+1)]:   # 문자열의 처음과 끝을 검사하는데 인덱스 한칸씩 안으로 줄어들면서 검사
            return "no"                 # 회문이 아니면 no 출력
    return "yes"                        # 회문이 맞으면 yes 출력

word = input('단어를 입력하세요: ')
print(Palindromedis(word))
