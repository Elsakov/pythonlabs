price=float(input())
discount=float(input())
vat=float(input())
base=price*(1-discount/100)
vat_amout=base*(vat/100)
total=base+vat_amout
print("База после скидки:", base)
print("НДС:", vat_amout)
print("Итого к оплате:", total)