A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {'i'}

# works as (A).symmetric_difference(B)
print(A ^ B)

# symmetric difference of 3 sets
print(A ^ B ^ C)