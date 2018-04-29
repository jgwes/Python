
# Examples of list functions
breeds = ['dachshund','doberman','schnauser','german shepard','dachshund']

print('Count of dachsunds: ', breeds.count('dachshund'))

print('List of breeds: ', breeds)

idx = input('Enter breed index to fetch: ')
print(idx, ' is at index ', breeds.index(idx))

print('List of Breeds: ', breeds)
breeds.reverse()
print('List of breeds in reverse ', breeds)

breeds.append('sheepdog')

print('Added sheepdog ', breeds)

breeds.sort()

print('Sorted breeds ', breeds)
print('Pop breed off stack ', breeds.pop())
print('Breeds after pop', breeds)
