#                1.제목:한국외대 자료구조 과제 6(6-1-1)
#                2.날짜:20210605
# 사전 해싱
class DoubleHashing:
    def __init__(self, size):
        self.M = size
        self.hash_table = [None for x in range(size+1)]  # hashtable
        self.data = [None for x in range(size+1)]  # key관련 data저장
        self.N = 0  # 항목수

    def getkey(self, key):   # 키를 [0]알파벳의 아스키코드값으로 받음
        self.key = ord(key[0])
        return self.key

    def hash_func(self, key):
        return key % self.M

    def getAddress(self, key):   # 해시값을 구함 인덱스 번호
        myKey = self.getkey(key)
        hash_address = self.hash_func(myKey)
        return hash_address

    def put(self, key, data):  # 단어 삽입 함수
        init_num = self.getAddress(key)  # 초기 위치
        i = init_num  # 초기 인덱스
        second_i = 7 - (self.getkey(key) % 7)  # hash 2
        j = 0
        while True:
            if self.hash_table[i] == None:  # 삽입 위치 찾기
                self.hash_table[i] = key  # key를 해쉬 테이블에 저장
                self.data[i] = data  # key값이 데이터를 동일한 인덱스에 저장
                self.N += 1
                return True
            elif self.hash_table[i] != None:  # 해시값에 data가 있는경우
                if self.hash_table[i] == key:  # 입력받은 키와 기존의 키가 같으면
                    return print("error1")   # error1출력
            if self.hash_table[i] == key:
                self.data[i] = data  # data 갱신
                return True
            j += 1
            i = (init_num + j*second_i) % self.M  # 충돌시 이중해쉬 하는 부분
            if self.N > self.M:  # 테이블이 꽉찰 경우
                break
        return print("error1")

    def get(self, key):  # 검색
        init_num = self.getAddress(key)
        i = init_num
        second_i = 7 - (self.getkey(key) % 7)
        j = 0
        while self.hash_table[i] != None:
            if self.hash_table[i] == key:  # 사전에서 단어를 검색하여
                return self.data[i]   # 뜻을 출력
            j += 1
            i = (init_num + j*second_i) % self.M
        return print("error2")   # 단어가 사전에 없을 경우 error2 출력

    def correct(self, key, data):  # 당어 뜻 수정 함수
        init_num = self.getAddress(key)
        i = init_num
        second_i = 7 - (self.getkey(key) % 7)
        j = 0
        while self.hash_table[i] != None:
            if self.hash_table[i] == key:  # key가 일치할경우
                self.data[i] = data   # 입력받은 data로 수정
                return
            j += 1
            i = (init_num + j * second_i) % self.M
        return print("error2")  # 단어가 사전에 없을 경우 error2 출력

    def print_table(self):   # 사전 출력 ( 쓰이진 않음)
        for i in range(self.M):
            if self.hash_table[i] == None:
                pass
            else:
                print(str(self.hash_table[i]) + str(self.data[i]))



h = DoubleHashing(13)
while True:
    command = input().split()
    #print(command)
    if command[0] == '단어삽입':
        h.put(command[1], command[2])
    elif command[0] == '단어뜻수정':
        h.correct(command[1], command[2])
    elif command[0] == '단어검색':
        print(h.get(command[1]))
    elif command[0] == 'p':  # 사전 확인용
        h.print_table()
    elif command[0] == '종료':  # 종료
        break

'''
단어삽입 time 시간
단어삽입 bee 벌
단어삽입 zoo 동물원
단어삽입 school 학기
단어삽입 trade 무역
단어삽입 farm 농장
단어삽입 zoo 동물원		
단어뜻수정 schol 학교
단어뜻수정 school 학교
단어검색 school
종료
'''