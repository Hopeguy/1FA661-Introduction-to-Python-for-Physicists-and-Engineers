# NEW FILE TO TRY STUFF IN

#---------Normalize a list --------

a = (2, 4, 10, 6, 8, 4)
a_norm = list(a)

for t, i in enumerate(a):
    a_norm[t] = (i-min(a))/(max(a)-min(a))
print(a_norm)


# ------FizzBuzz----------

n = 100

for i in range(1,n,1):
    if not i % 3 and i % 5:
        print('fizzbuzz')
    elif not i % 5:
        print('buzz')
    elif not i % 3:
        print('fizz')
    else:
        print(i)

