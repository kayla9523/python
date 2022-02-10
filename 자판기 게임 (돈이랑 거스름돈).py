#음료수 자판기 게임(가격 알려줌)
print("""커피 종류를 선택하시오.
1.아메리카노
2.카페라떼
3.핫초코""")
coffee= int(input("무슨 커피를 드실 것입니까?"))  
money = int(input("몇잔을 드실 것입니까?"))
a=0

if coffee == 1:
    a = 1800
if coffee == 2:
    a = 2700
if coffee == 3:
    a = 2300
print("총액은",a*money)
money2= int(input("돈을 투입해주세요"))
print(money2 - a*money)
g = money2 - a*money
cw=g//1000 #천원 추출 
cwl=g%1000 #천원 추출하고 남은것들 
ow=cwl//500 #500원 추출 
bw=cwl%500#500원  추출하고 남은것들
bwl= bw//100

print("천원:",cw,"오백원:",ow,"백원:",bwl)
