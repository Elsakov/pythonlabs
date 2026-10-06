def min_max(n):
    if len(n) == 0:
        return "ValueError (список не может быть пустым)"
    minim = n[0]
    maxim = n[0]
    for n in n[1:]:
        if n < minim:
            minim = n
        if n > maxim:
            maxim = n
    return minim, maxim

def unique_sorted(un):
    res = []            
    for n in un:          
        if n not in res:
            res.append(n)
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if res[i]>res[j]:
                res[i],res[j] = res[j],res[i]       
    return res
def flatten(r):
    for row in r:
        if not isinstance(row, (list, tuple)):   # <-- разрешаем и list, и tuple
            return "TypeError («строка не строка строки матрицы»)"
    res = []
    for row in r:
        for e in row:
            res.append(e)
    return res
print("min_max")
print("[3, -1, 5, 5, 0] ->", min_max([3, -1, 5, 5, 0]))
print("[42] ->", min_max([42]))
print("[-5, -2, -9] ->", min_max([-5, -2, -9]))
print('[] ->', min_max([]))
print("[1.5, 2, 2.0, -3.1] ->", min_max([1.5, 2, 2.0, -3.1]))

print("unique_sorted")
print("[3, 1, 2, 1, 3] -> " + str(unique_sorted([3, 1, 2, 1, 3])))
print("[] -> " + str(unique_sorted([])))
print("[-1, -1, 0, 2, 2] -> " + str(unique_sorted([-1, -1, 0, 2, 2])))
print("[1.0, 1, 2.5, 2.5, 0] -> " + str(unique_sorted([1.0, 1, 2.5, 2.5, 0])))

print("flatten")
print("[[1, 2], [3, 4]] -> " + str(flatten([[1, 2], [3, 4]])))
print("[[1, 2], (3, 4, 5)] -> " + str(flatten([[1, 2], (3, 4, 5)])))
print("[[1], [], [2, 3]] -> " + str(flatten([[1], [], [2, 3]])))
print('[[1, 2], "ab"] ->', flatten([[1, 2], "ab"]))