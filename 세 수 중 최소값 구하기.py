#세수 중 최소값 찾기
a = int(input("첫번째 숫자 입력"))
b = int(input("두번째 숫자 입력"))
c = int(input("세번째 숫자 입력"))

if a<b and a<c:
    print(a,"는 최소값")
if b<a and b<c:
    print(b,"는 최소값")
if c<b and c<a:
    print(c,"는 최소값")
