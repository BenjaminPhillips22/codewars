# https://www.codewars.com/kata/data-reverse


def data_reverse(data):
    list_of_lists = []
    for l in range(int(len(data)/8)):
        list_of_lists.append([data[d] for d in range(l*8, l*8 + 8)])
    return [a for b in list_of_lists[::-1] for a in b]


# tests
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

print(data_reverse(data1))
print(data_reverse(data1) == data2)
