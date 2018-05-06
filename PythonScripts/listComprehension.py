# consists of brackets containing an expression followed by 
# a for clause, then zero or more for or if clauses
# result is a new list resulting from evaluating the in the context of the
# for and if clauses which follow it. 

# squares / list comprehension example
squares = [x**2 for x in range(10)]
print(squares)

# combine elements of two liss if they are not equal
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y])
