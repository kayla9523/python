#예제3번
b=[0,0,0,0,0]
while True:
    a= int(input("10부터 59사이의 수를 입력하시오"))
    if a == 0:
        break
    if a//10==1:
        b[0]+=1
    elif a//10==2:
        b[1]+=1
    elif a//10 == 3:
        b[2]+=1
    elif a//10==4:
        b[3]+=1
    elif a//10 ==5:
        b[4]+=1
print(b)
        

    
