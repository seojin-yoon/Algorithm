#병합정렬
#n(1이상 500000 이하 정수)개의 정수들에 대하여 두 수 차의 최솟값을 구하시오.

n=int(input()) #입력의 크기
List=list(map(int, input().split())) #변수를 입력받음

def MergeSort(num):

    n = len(num) #리스트 크기

    if n <= 1: #정렬할 원소가 하나 이하이면 정렬 끝
        return

    mid = n // 2 #중간 인덱스값
    leftSet = num[:mid] 　#mid보다 왼쪽에 있는 값들의 리스트
    rightSet = num[mid:]  #mid보다 오른쪽에 있는 값들의 리스트

    MergeSort(leftSet)　#병합정렬
    MergeSort(rightSet)

    left = 0
    right = 0
    now = 0

    while left < len(leftSet) and right < len(rightSet): #left가 mid 왼쪽값의 리스트 길이보다 작고 right가 오른쪽값의 리스트보다 작을 때
        if leftSet[left] < rightSet[right]:
            num[now] = leftSet[left]
            left += 1
            now += 1
        else:
            num[now] = rightSet[right]
            right += 1
            now += 1

    while left < len(leftSet): #left가 mid 왼쪽값의 리스트 길이보다 작을 때
        num[now] = leftSet[left]
        left += 1
        now += 1

    while right < len(rightSet): #right가 mid 오른쪽값의 리스트 길이보다 작을 때 
        num[now] = rightSet[right]
        right += 1
        now += 1

MergeSort(List) #병합정렬 호출
Min = List[1] - List[0] 
for i in range(2,n): #연속된 두 수의 차 비교하는 반복문
	current = List[i] - List[i-1]
	if Min > current:
		Min = current
	
print(Min) #최솟값 출력
