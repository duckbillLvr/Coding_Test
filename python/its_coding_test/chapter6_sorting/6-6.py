# 계수 정렬 (비둘기집 정렬)
'''
사용 조건
1. 정수 형태로 표현할 수 있을 때
2. 크기가 1,000,000 이하일때 효율적이다.
'''

# 모든 원소의 값이 0 이상이라 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]): # 인덱스에 저장된 수 만큼 출력
        print(i, end=' ')