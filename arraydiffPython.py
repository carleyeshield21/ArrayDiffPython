# This is the link to this Python coding challenge
# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    arr = []
    for i in a:
        counter = 0
        for j in b:
            # print(i, j)
            if i == j:
                counter += 1
        if counter == 0:
            arr.append(i)
        # print(f'Counter = {counter}')
    print(f'a = {a}\nb = {b}')
    print(arr)
    # print(counter)
array_diff([1, 2, 2, 2, 3], [2,1,3])
print('========')
array_diff([1, 2], [1])