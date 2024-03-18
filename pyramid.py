x = int(input())
i = 1
back = False
while True:
    if i == x+1:
        i = x-1
        back = True
    if back == False: 
        print('*'*i)
        i += 1
    elif back == True:
        if i == 0:break
        print('*'*i)
        i -= 1