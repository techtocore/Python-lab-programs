import numpy as np

a = [1, 2, 3, 4]
print("Original array")
print(a)
print("Enter no of times to repeat while appending")
n=2;
for _ in range(int(input())):
    print("Repeating " + repr(n) +  " times")
    x = np.tile(a, n)
    print(x)
    n=n+1
