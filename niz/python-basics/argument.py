# * args and **kwargs
# arg = (1,2,3)
# Tuple : immutable
def sum_numbers(*args):
    answer = 0 # 1
    for num in args: # 1 , 2 ,3 
        answer = answer + num
    return answer

print(sum_numbers(1,2,3))

# TODO List -> sum_numbers

# Kwargs
def concat_string(**kwargs):
    answer = ''
    for string in kwargs.values():
        answer += string
    return answer

print(concat_string(a="My",b="name",c="is",d="Niz"))

