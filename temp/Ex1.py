# Ctrl Shift a to use the useful arepl in vs code (you are gonna like it)

#$end

print("\nRead a file")
filename = "data.txt"
text = "".join([line for line in open(filename)])
print(text)
text = acc = ""; [acc := acc + line for line in open(filename)]
print(text)


print("\nSound with chime")
import chime
chime.theme('mario')

# chime.warning()
# chime.error()
# chime.info()
chime.success()


print("\nTranspose a matrix")

import numpy as np
nums = [[1,2,3], [4,5,6], [7,8,9]]
transpose_matrix = [list(item) for item in zip(*nums)]
print(transpose_matrix)
mat = np.matrix(nums)
print(mat)
transpose_matrix_2 = np.transpose(mat)
print(transpose_matrix_2)

print("\nFibonacci")
n = 10
fib1 = [1, 2]
[fib1.append(fib1[-1]+fib1[-2]) for _ in range(n-2)]
fib1
l = len(fib1)

from itertools import count
pairs = dict(zip(count(1), fib1))


print("\nList from the input separated by comma")

standard_input = "1,2,3,4,5,6,7,8,9,10,11"
splited_input = list(map(int, input().split(",")))
print(splited_input)


print("\nSum of the number's digits")
digits_sum_fun = lambda x: sum(map(int, str(x)))
digits_sum = digits_sum_fun(123)
print(digits_sum)

print("\nFlatten")
numbers = [[1], [2,3], [4,5,6], [7,8,9]]
flatten = [item for sublist in numbers for item in sublist]
print(flatten)

print("\nReversed string")
str = "Hello, world!"
reversed = str[::-1]
print(reversed)

print("\nMerged maps")
dic1 = {"Tony": 52, "Liviu": 39}
dic2 = {"Irina": 31, "Roxana": 36}
siblings = {**dic1, **dic2}
print(siblings)

print("\nSwapped maps")
swapped  = {v:k for k, v in siblings.items()}
print(swapped)

