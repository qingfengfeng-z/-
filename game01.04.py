import random
print('来玩游戏啊')

while True:
    secret=random.randint(1,100)
    i=0
    result=True
    
    while True:
        i=i+1
        if i==1:
            number=input('输入一个数')
        else:
            number=input('辣鸡重猜')
        guess=int(number)
 
        if guess==secret:
            print('bingo!')
            result=False
            break
        else:
            if guess>secret:
                print('大了大了')
            else:
                print('小了小了')
        if i>=5:
            print('已经猜了'+str(i)+'次都没中，你是居居嘛？')
            result=True
            break
        

    if not result:
        others=input('好厉害！！要不要再来？继续输入y任意键退出')
    else:
        others=input('辣鸡再来？继续输入y任意键退出')
        
    if others!='y':
        break
        
print('Game Over!')
