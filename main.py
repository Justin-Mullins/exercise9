'''

Exerciese 9:
First-Last

We’ll practice these ideas with this exercise. Write a function, firstlast , that takes
a sequence (string, list, or tuple) and returns the first and last elements of that
sequence, in a two-element sequence of the same type. So firstlast('abc') will
return the string ac , while firstlast([1,2,3,4]) will return the list [1,4] .

'''
def firstlast(sequence):
    return sequence[0:1] + sequence[-1:]

print(firstlast('Tiger'))
print(firstlast([0, 1, 2, 3, 4, 7]))
print(firstlast(('ace', 'queen', 'king', 'jack', 'ten')))