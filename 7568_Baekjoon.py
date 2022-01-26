N = int(input())
data = []
ans = [] #리스트는 대괄호

for i in range(N):
    weight, height = map(int,input().split())
    data.append((weight, height)) #튜플은 소괄호
for i in range(N):
    cnt = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: #몸무게끼리 비교, 키끼리 비교해서
            #(몸무게가 작으면, 키가 작으면) 랭킹을 증가시킴
            cnt = cnt+1                                         #리스트와 튜플은 참조방법이 []대괄호로 같은가?
    ans.append(cnt+1)

for a in ans:
    print(a, end=' ')
