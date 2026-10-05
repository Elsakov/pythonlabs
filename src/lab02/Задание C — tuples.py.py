def format_record(r):
    if not isinstance(r, tuple) or len(r) != 3:
        raise TypeError("Ожидается кортеж из 3 элементов")
    f, g, p = r
    if not isinstance(f, str) or not isinstance(g, str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(p, (int, float)):
        raise TypeError("GPA должен быть числом")
        
    fp = " ".join(f.split()).split()
    gr = g.strip()
    
    if not fp:
        raise ValueError("ФИО не может быть пустым")
    if not gr:
        raise ValueError("Группа не может быть пустой")
    if not (0.0 <= p <= 5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")
        
    s = fp[0].capitalize()
    i = ""
    for n in fp[1:]:
        if n:
            i += n[0].upper() + "."
            
    ps = "{:.2f}".format(p)
    res = s + " " + i + ", гр. " + gr + ", GPA " + ps
    return res

print("Задание C — tuples.py")
print()
print('("Иванов Иван Иванович", "BIVT-25", 4.6) -> ' + format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print('("Петров Пётр", "IKBO-12", 5.0) -> ' + format_record(("Петров Пётр", "IKBO-12", 5.0)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0) -> ' + format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print('(" сидорова анна сергеевна ", "ABB-01", 3.999) -> ' + format_record((" сидорова анна сергеевна ", "ABB-01", 3.999)))
