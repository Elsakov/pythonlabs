def transpose(m):
    if not m:
        return []
    
    c = len(m[0])
    for r in m:
        if len(r) != c:
            raise ValueError("Матрица не прямоугольная")
            
    o = []
    for j in range(c):
        nr = []
        for i in range(len(m)):
            nr.append(m[i][j])
        o.append(nr)
    return o

def row_sums(m):
    if not m:
        return []
        
    c = len(m[0])
    for r in m:
        if len(r) != c:
            raise ValueError("Матрица не прямоугольная")    
    o = []
    for r in m:
        s = 0
        for v in r:
            s += v
        o.append(s)
    return o

def col_sums(m):
    if not m:
        return []       
    c = len(m[0])
    for r in m:
        if len(r) != c:
            raise ValueError("Матрица не прямоугольная")     
    o = []
    for j in range(c):
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        o.append(s)
    return o
print("transpose")
print("[[1, 2, 3]] ->", transpose([[1, 2, 3]]))
print("[[1], [2], [3]] ->", transpose([[1], [2], [3]]))
print("[[1, 2], [3, 4]] ->", transpose([[1, 2], [3, 4]]))
print("[] ->", transpose([]))
print("[[1, 2], [3]] -> ValueError (равная матрица)")

print("\nrow_sums")
print("[[1, 2, 3], [4, 5, 6]] ->", row_sums([[1, 2, 3], [4, 5, 6]]))
print("[[-1, 1], [10, -10]] ->", row_sums([[-1, 1], [10, -10]]))
print("[[0, 0], [0, 0]] ->", row_sums([[0, 0], [0, 0]]))
print("[[1, 2], [3]] -> ValueError (равная)")

print("\ncol_sums")
print("[[1, 2, 3], [4, 5, 6]] ->", col_sums([[1, 2, 3], [4, 5, 6]]))
print("[[-1, 1], [10, -10]] ->", col_sums([[-1, 1], [10, -10]]))
print("[[0, 0], [0, 0]] ->", col_sums([[0, 0], [0, 0]]))
print("[[1, 2], [3]] -> ValueError (равная)")