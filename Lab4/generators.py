# # 1
# def squgen(n):
#     for i in range(1, n+1):
#         yield i*i
    
# num = int(input("esli natural napishi naturalnoe chislo: "))
# for i in squgen(num):
#     print (i)

# # 2
# def eve(n):
#     for i in range(0 , n+1 , 2):
#         yield i

# num = int(input("esli natural napishi naturalnoe chislo eshe raz: "))
# ans = [str(i) for i in eve(num)]
# print(",".join(ans))

# # 3
# def div(n):
#     for i in range(0, n+1):
#         if(i%3 == 0 and i%4 == 0): 
#             yield i

# num = int(input("esli natural napishi naturalnoe chislo tretiy raz: "))

# for i in div(num):
#     print (i)

# # 4
# def squarepants(a , b):
#     for i in range(a, b + 1):
#         yield i*i

# num1 = int(input("napishi nachalnoe chislo: "))
# num2 = int(input("napishi konechnoe chislo: "))
# for i in squarepants(num1,num2):
#     print (i)

# 5
def rev(n):
    for i in range(0 , n+1):
        yield i

num = int(input("esli natural napishi naturalnoe chislo snova: "))
lst = []
for i in rev(num):
    lst.append(i)

print (*lst[::-1])

def rev2(n):
    while n != -1:
        yield n
        n -= 1

num = int(input("esli natural napishi naturalnoe chislo snova: "))
for i in rev2(num):
    print (i)
