#이진탐색 문제
#오름차순으로 정렬된 n개의 정수 중 정수 k와 가장 가까운 정수를 찾는 프로그램
#단, K와 가장 가까운 정수가 여러 개일 경우, 큰 수를 출력해야함.

n = int(input()) # 입력의 크기
List = list(map(int,input().split())) # 정수를 입력받는다
k = int(input())

def binarySearch(A, key): # 이진탐색 이용해서 key값에 가장 가까운 두 값을 반환하는 함수
													# A는 리스트, key는 k
	if len(A) == 1: # base case: 리스트 원소가 하나일 때
		return(A[0],A[0])
	elif len(A) == 2: # base case: 리스트 원소가 두개일 때
		return(A[0],A[1])
	
	left = 0
	right = len(A)-1
	
	mid = (left+right)//2 # mid는 리스트 중앙 인덱스값
	
	if A[mid] <= key: # 중앙값이 key보다 작을 때
		return binarySearch(A[mid:],key)
	else: # 중앙값이 key보다 클 때
		return binarySearch(A[:mid+1],key)
	
def findNearest(A,key): # 가장 가까운 정수 찾는 함수
	items = binarySearch(A,key)				# binarySearch 함수 호출
	if (key - items[0]) == (items[1] - key): # key와 가장 가까운 정수가 여러개일 때, 큰 수 출력
		return items[1]
	elif (key - items[0]) > (items[1] - key): # key보다 작은 값이 key보다 큰 값보다 key값에 가까울 때
		return items[1]
	else:					# key보다 큰 값이 key보다 작은 값보다 key값에 가까울 때
		return items[0]
	

print(findNearest(List, k))
