# https://www.codewars.com/kata/equal-sides-of-an-array


def find_even_index(arr):
    a = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[1+i:])]
    if a == []:
        return -1
    return a[0]


# tests

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,2,3,4,3,2,1]) == 3)
print(find_even_index([1,100,50,-51,1,1]) == 1)
print(find_even_index([1,2,3,4,5,6]) == -1)
print(find_even_index([20,10,30,10,10,15,35]) == 3)
print(find_even_index([20,10,-80,10,10,15,35]) == 0)
print(find_even_index([10,-80,10,10,15,35,20]) == 6)

# other solutions


def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
    return r[0] if r else -1
