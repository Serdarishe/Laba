a = [1, 2, 3, 4, 5]

def func(a):
    cnt = 0
    sum = 0
    for i in a:
        sum += i
        cnt +=1
    return(sum/cnt)

print(func(a))