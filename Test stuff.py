import math
# t = [3, 4]
# math.hypot(t[0],t[1])
# print(math.hypot(*t))
# print( '\n')


# # Fibonatchi seq for n values

# n = 100
# fib =[0,1]
# for i in range(2, n+1, 1):
#     fib.append(fib[i-1] + fib[i-2])
# print(fib)

# food = ['ice cream', 'burgers', "hot dog"]
# for i, food in enumerate(food, 4):
#     print(i, ":", food)
    

# s = 'hello'
# a = [4, 10 ,2]

# print(list(range(*a)))

# P= [4, 5, 0, 2]
# dPdx = []
# for i, c in enumerate(P):
#     dPdx.append(i*c)
#     print(i, c)
# print(dPdx)

# ------------Madhava series pi estimation #1 
#
# n= 20 
# n2 = 5 + 2*n
# a= list(range(5,n2,2))
# madhava_series = 1
# for i, t in enumerate(a,1):
#     if (i % 2) == 0:
#         madhava_series = madhava_series + (1/(t*(3**i)))
#     else:
#         madhava_series = madhava_series - (1/(t*(3**i)))
#    # print(t, i)
#    # print(madhava_series)
# pi = math.sqrt(12)*(madhava_series)
# print(pi)


# --------Madhava series number #2----------
# n = 2000000
# n2 = 3 + 2*n
# a_2= list(range(3,n2,2))
# pi = 1
# for i, t in enumerate(a_2):
#     if (i % 2) == 0:
#         pi = pi - (1/t)
#     else:
#         pi = pi + (1/t)

# print(pi*4)

# -----------Different methods for multiplying list with iself------
# a = [1, 2, 3, 4, 5, 6, 7]
# p =[]
# t = 0
# while t < len(a):
#     p_i = 1
#     for i in a:
#         p_i = p_i*i
#     p.append(p_i/a[t])
#     t += 1
# print(p)


# a = [1, 2, 3]
# k =[]
# for i in a:
#    k.append(math.prod(a)/i)  
# print(k)

# a = (1, 2, 3)
# k = list(a)
# t = 0
# for i in a:
#     k[t] = math.prod(a)/i
#     t += 1
# print(k)

# a = (1, 2, 3)
# k = list(a)
# for t, i in enumerate(a):
#     k[t] = math.prod(a)/i
# print(k)


# def divide(x):
#     return k/x

# a = [1, 2, 3, 4, 5]
# for i in a:
#     k = math.prod(a)
# F = list(map(divide, a))
# print(F)


#--------------------