def find_largest_rect(heights):
    stack = [] #스택 초기화
    max_area = 0 #최대 직사각형 넓이 초기화

    for i in range(len(heights)): #각 빌딩에 대해 반복
        while stack and heights[i] < heights[stack[-1]]: #현재 빌딩이 스택의 맨 위의 빌딩보다 작은 경우
            height = heights[stack.pop()] #스택에서 이전의 빌딩을 빼고 해당 빌딩을 높이로 함
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width) #넓이 계산
        stack.append(i) #현재 빌딩 인덱스를 스택에 추가

    while stack: #스택에 남아있는 빌딩
        height = heights[stack.pop()]#스택에서 이전의 빌딩을 빼고 해당 빌딩을 높이로 함
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width) #최대 직사각형 넓이

    return max_area

if __name__ == "__main__":
    n = int(input())
    building_heights = list(map(int, input().split()))
    result = find_largest_rect(building_heights)
    print(result)

# for문은 입력 받은 빌딩의 수에 비례한다. 
# 각 빌딩에 대해 O(1) 시간 작업을 수행하므로 전체 루프의 시간 복잡도는 O(n)이다. 
# 내부의 스택에 남아있는 빌딩을 처리하는 while문에서는 스택이 비어있지 않을 때만 실행된다. 
# 각 빌딩은 한 번 스택에 들어가고 한 번 스택에서 빠져나오므로 실행 횟수는 O(n)이다. 