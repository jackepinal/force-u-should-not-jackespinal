#print list assertions
# Below is our test code. Do not modify it, but you may add your own prints.
#this is a form of debugging
assert(is_permutation([1, 2, 3], [3, 1, 2]) == True)
assert(is_permutation([1, 1, 1, 2],[1, 2, 1, 1]) == True)
assert(is_permutation([1, 2, 3, 1], [1, 2, 3]) == False)
assert(is_permutation([1, 1, 2, 3], [1, 3, 2, 2]) == False)