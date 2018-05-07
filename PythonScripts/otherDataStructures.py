# set - eliminates dups. create with set() function or curly braces
# empty set requires set()
basket = {'apple','orange','apple','cranberries','avacado'}
print(basket)

# membership test
if 'apple' in basket:
    print('apple in basket')
else:
    print('applie not in basket')

# Set operations
a = set('abracadabra')
b = set('alacazam')
print('Create sets \'abracadabra\' and \'alacazam\'')
print('Set one ', a)
print('Set two ', b)

# in a but not b
c = a - b
print('in a but not b ', c)

# union
d = a | b
print('union ', a | b)

# intersect
e = a & b
print('intersect a and b ', e)

# XOR
f = a ^ b
print('a XOR b ', f)


# set comprehension
a = { x for x in 'abracadabra' if x not in 'abc'}
print(a)

