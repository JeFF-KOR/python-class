def func(x:int,y:int)-> int:
    return x+y
# print(func(1,2))
f = lambda x,y : x+y
# print(f('1','2'))
x = f(1,2)
# Python3.8 >= 
# print(f'{x=}')

print(list(filter(lambda x: x%2 ==0, [1,2,3,4,5,6,7,8,9,10])))
for x in [1,2,3,4,5,6,7,8,9,10]:
    if x%2 == 0:
        print(x)

test = lambda x: True if(x>10 and x<20) else False

print(test(12))
print(test(9))
