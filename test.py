import random as rd
x = 1
# x = 'aaaa'
# x = ['a','b','c']
# x = {
#     'a':'10',
#     'b':'10'
# }
x = rd.randint(0,100)
arr = []
for i in range(0,10):
    i = rd.randint(1,100)
    arr.append(i)

print('***********',arr,'**************')
print('***********',type(x),'**************')