squares = []
for x in range(10):
    print(x**2)
    squares.append(x**2)

print(squares)


# or lambda
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# or more simply
squares = [x**2 for x in range(10)]
print(squares)
