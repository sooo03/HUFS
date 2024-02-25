import time, random

# code for O(n^2)-time version
def compute_e_ver1(n):
    result = 1
    for i in range(n):
        d = 1
        for j in range(0, i+1):
            d *= j + 1
        result += 1/d
        # time check
        after = time.process_time()
        if (after - before1) > 60:
            print('over time')
            break
    return result
            

# code for O(n)-time version
def compute_e_ver2(n):
    result = 1
    d = 1
    for i in range(n):
        d *= i + 1
        result += 1/d
        after = time.process_time()
        if (after - before2) > 60:
            print('over time')
            break
    return result
# n 입력받음

n = int(input("수 입력: "))

# compute_e_ver1 호출

before1 = time.process_time()
print(f'answer: {compute_e_ver1(n)}')
after1 = time.process_time()
print(f'time : {after1 - before1}')

# compute_e_ver2 호출
before2 = time.process_time()
print(f'answer: {compute_e_ver2(n)}')
after2 = time.process_time()
print(f'time : {after2 - before2}')
# 두 함수의 수행시간 출력
